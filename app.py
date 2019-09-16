from flask import Flask, Response, jsonify
import waitress
from gbfs.services import SystemDiscoveryService


app = Flask(__name__)

ds = SystemDiscoveryService()


@app.route('/app/api/v1.0/systems', methods=['GET'])
def systems():
    return jsonify(ds.systems)


@app.route('/app/api/v1.0/system/<string:system_id>', methods=['GET'])
def system_detail(system_id):
    data = ds.get_system_by_id(system_id)
    return jsonify(data)


@app.route('/app/api/v1.0/system/<string:system_id>/feeds', methods=['GET'])
def system_feeds(system_id):
    client = ds.instantiate_client(system_id)
    return jsonify(client.feed_names)


@app.route('/app/api/v1.0/system/<string:system_id>/feed/<feed_name>', methods=['GET'])
def system_feed_detail(system_id, feed_name):
    client = ds.instantiate_client(system_id)
    return jsonify(client.request_feed(feed_name))


@app.route('/app/api/v1.0/system/<string:system_id>/station/<string:station_id>', methods=['GET'])
def system_station_detail(system_id, station_id):
    client = ds.instantiate_client(system_id)
    if client is None:
        return Response(status=404)

    station_feed = client.request_feed('station_information')
    status_feed = client.request_feed('station_status')

    all_stations = station_feed.get('data').get('stations')
    all_statuses = status_feed.get('data').get('stations')

    try:
        station = next(filter(lambda x: str(x.get('station_id')) == station_id, all_stations))
        id_join = str(station.get('station_id'))
        status = next(filter(lambda x: str(x.get('station_id')) == id_join, all_statuses))
    except StopIteration:
        return Response(status=404)

    result = {'last_updated': status_feed.get('last_updated'), 'ttl': status_feed.get('ttl')}
    result.update(station)
    result.update(status)

    return jsonify(result)


def main():
    waitress.serve(app)


if __name__ == '__main__':
    main()
