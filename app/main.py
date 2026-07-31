from typing import Any

import uvicorn
from fastapi import FastAPI, HTTPException
from gbfs.services import SystemDiscoveryService


app = FastAPI(
    title='bikeshare-json-api',
    description='A simple json api for polling live GBFS bikeshare feeds, implementing the gbfs-client pip package (source: jakehadar/bikeshare-client-python).',
)

ds = SystemDiscoveryService()


@app.get('/app/api/v1.0/systems')
def systems() -> Any:
    return ds.systems


@app.get('/app/api/v1.0/system/{system_id}')
def system_detail(system_id: str) -> Any:
    result = ds.get_system_by_id(system_id)
    if result is None:
        raise HTTPException(status_code=404)

    return result


@app.get('/app/api/v1.0/system/{system_id}/feeds')
def system_feeds(system_id: str) -> Any:
    client = ds.instantiate_client(system_id)
    if client is None:
        raise HTTPException(status_code=404)

    return client.feed_names


@app.get('/app/api/v1.0/system/{system_id}/feed/{feed_name}')
def system_feed_detail(system_id: str, feed_name: str) -> Any:
    client = ds.instantiate_client(system_id)
    if client is None:
        raise HTTPException(status_code=404)

    result = client.request_feed(feed_name)
    if result is None:
        raise HTTPException(status_code=404)

    return result


@app.get('/app/api/v1.0/system/{system_id}/stations')
def system_stations(system_id: str) -> Any:
    client = ds.instantiate_client(system_id)
    if client is None:
        raise HTTPException(status_code=404)

    result = client.request_feed('station_information').get('data').get('stations')
    return result


@app.get('/app/api/v1.0/system/{system_id}/station/{station_id}/information')
def system_station_status(system_id: str, station_id: str) -> Any:
    client = ds.instantiate_client(system_id)
    if client is None:
        raise HTTPException(status_code=404)

    feed = client.request_feed('station_information')
    items = feed.get('data').get('stations')

    try:
        result = next(filter(lambda x: str(x.get('station_id')) == station_id, items))
    except StopIteration:
        raise HTTPException(status_code=404)

    result.update({'last_updated': feed.get('last_updated'), 'ttl': feed.get('ttl')})
    return result


@app.get('/app/api/v1.0/system/{system_id}/station/{station_id}/status')
def system_station_information(system_id: str, station_id: str) -> Any:
    client = ds.instantiate_client(system_id)
    if client is None:
        raise HTTPException(status_code=404)

    feed = client.request_feed('station_status')
    items = feed.get('data').get('stations')

    try:
        result = next(filter(lambda x: str(x.get('station_id')) == station_id, items))
    except StopIteration:
        raise HTTPException(status_code=404)

    result.update({'last_updated': feed.get('last_updated'), 'ttl': feed.get('ttl')})
    return result


@app.get('/app/api/v1.0/system/{system_id}/station/{station_id}')
def system_station_detail(system_id: str, station_id: str) -> Any:
    client = ds.instantiate_client(system_id)
    if client is None:
        raise HTTPException(status_code=404)

    station_feed = client.request_feed('station_information')
    status_feed = client.request_feed('station_status')

    all_stations = station_feed.get('data').get('stations')
    all_statuses = status_feed.get('data').get('stations')

    try:
        station = next(filter(lambda x: str(x.get('station_id')) == station_id, all_stations))
        id_join = str(station.get('station_id'))
        status = next(filter(lambda x: str(x.get('station_id')) == id_join, all_statuses))
    except StopIteration:
        raise HTTPException(status_code=404)

    result = {'last_updated': status_feed.get('last_updated'), 'ttl': status_feed.get('ttl')}
    result.update(station)
    result.update(status)

    return result


def main():
    uvicorn.run(app)


if __name__ == '__main__':
    main()
