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
    result = ds.get_system_by_id(system_id)
    if result is None:
        return Response(status=404)

    return jsonify(result)


@app.route('/app/api/v1.0/system/<string:system_id>/feeds', methods=['GET'])
def system_feeds(system_id):
    client = ds.instantiate_client(system_id)
    if client is None:
        return Response(status=404)

    return jsonify(client.feed_names)


@app.route('/app/api/v1.0/system/<string:system_id>/feed/<feed_name>', methods=['GET'])
def system_feed_detail(system_id, feed_name):
    client = ds.instantiate_client(system_id)
    if client is None:
        return Response(status=404)

    result = client.request_feed(feed_name)
    if result is None:
        return Response(status=404)

    return jsonify(result)


@app.route('/app/api/v1.0/system/<string:system_id>/stations', methods=['GET'])
def system_stations(system_id):
    client = ds.instantiate_client(system_id)
    if client is None:
        return Response(status=404)

    result = client.request_feed('station_information').get('data').get('stations')
    return jsonify(result)


@app.route('/app/api/v1.0/system/<string:system_id>/station/<string:station_id>/information', methods=['GET'])
def system_station_status(system_id, station_id):
    client = ds.instantiate_client(system_id)
    if client is None:
        return Response(status=404)

    feed = client.request_feed('station_information')
    items = feed.get('data').get('stations')

    try:
        result = next(filter(lambda x: str(x.get('station_id')) == station_id, items))
    except StopIteration:
        return Response(status=404)

    result.update({'last_updated': feed.get('last_updated'), 'ttl': feed.get('ttl')})
    return jsonify(result)


@app.route('/app/api/v1.0/system/<string:system_id>/station/<string:station_id>/status', methods=['GET'])
def system_station_information(system_id, station_id):
    client = ds.instantiate_client(system_id)
    if client is None:
        return Response(status=404)

    feed = client.request_feed('station_status')
    items = feed.get('data').get('stations')

    try:
        result = next(filter(lambda x: str(x.get('station_id')) == station_id, items))
    except StopIteration:
        return Response(status=404)

    result.update({'last_updated': feed.get('last_updated'), 'ttl': feed.get('ttl')})
    return jsonify(result)


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
