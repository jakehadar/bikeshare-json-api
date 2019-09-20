bikeshare-demo-app
------------------

A json api for polling live Bikeshare feeds, demonstrating a simple [bikeshare-client-python](https://github.com/jakehadar/bikeshare-client-python) use-case.

The API spec is annotated in [app.py](https://github.com/jakehadar/bikeshare-demo-app/blob/master/app.py)


REST examples
-------------

1. Query all systems:

* [GET /systems](https://bikeshare.pythonanywhere.com/app/api/v1.0/systems)

* JSON Response (list of dictionaries, shortened for example): 
  ```json
  [
      {"Auto-Discovery URL":"https://gbfs.nextbike.net/maps/gbfs/v1/nextbike_bn/gbfs.json","Country Code":"DE","Location":"Berlin, DE","Name":"Deezer nextbike","System ID":"nextbike_bn","URL":"https://www.deezernextbike.de/xx/berlin/"},
      {"Auto-Discovery URL":"https://gbfs.citibikenyc.com/gbfs/gbfs.json","Country Code":"US","Location":"NYC, NY","Name":"Citi Bike","System ID":"NYC","URL":"https://www.citibikenyc.com"}, 
      {"Auto-Discovery URL":"https://sea.jumpbikes.com/opendata/gbfs.json","Country Code":"US","Location":"Seattle, WA","Name":"JUMP Seattle","System ID":"jump_seattle","URL":"https://jump.com"}
  ]
  ```

2. Select CitiBike ("System ID": "NYC"):

* [GET /system/NYC](https://bikeshare.pythonanywhere.com/app/api/v1.0/system/NYC)

* JSON Response (dictionary): 
  ```json
  {"Auto-Discovery URL":"https://gbfs.citibikenyc.com/gbfs/gbfs.json","Country Code":"US","Location":"NYC, NY","Name":"Citi Bike","System ID":"NYC","URL":"https://www.citibikenyc.com"}
  ```

3. List of feeds provided by CitiBike:

* [GET /system/NYC/feeds](https://bikeshare.pythonanywhere.com/app/api/v1.0/system/NYC/feeds)

* JSON Response (list of strings): 
  ```json
  ["station_information","system_regions","system_alerts","station_status","system_information"]
  ```

4. CitiBike system alerts (feed):

* [GET /system/NYC/feed/system_alerts](https://bikeshare.pythonanywhere.com/app/api/v1.0/system/NYC/feed/system_alerts)

* JSON Response (data structures vary by system and feed): 
  ```json
  {
      "data": {
          "alerts": []
      },
      "last_updated": "Fri, 20 Sep 2019 15:14:39 GMT",
      "ttl": 10
  }
  ```

5. Query all CitiBike stations:

* [GET /system/NYC/stations](https://bikeshare.pythonanywhere.com/app/api/v1.0/system/NYC/stations)

* JSON Response (list of dictionaries, shortened for example): 
  ```json
  [
      {"capacity":60,"eightd_has_key_dispenser":false,"electric_bike_surcharge_waiver":false,"external_id":"66db3606-0aca-11e7-82f6-3863bb44ef7c","has_kiosk":true,"lat":40.74334935,"lon":-74.00681753,"name":"W 16 St & The High Line","region_id":71,"rental_methods":["KEY","CREDITCARD"],"rental_url":"http://app.citibikenyc.com/S6Lr/IBV092JufD?station_id=212","short_name":"6233.05","station_id":"212"},
      {"capacity":23,"eightd_has_key_dispenser":false,"electric_bike_surcharge_waiver":false,"external_id":"66db3687-0aca-11e7-82f6-3863bb44ef7c","has_kiosk":true,"lat":40.70037867,"lon":-73.99548059,"name":"Columbia Heights & Cranberry St","region_id":71,"rental_methods":["KEY","CREDITCARD"],"rental_url":"http://app.citibikenyc.com/S6Lr/IBV092JufD?station_id=216","short_name":"4829.01","station_id":"216"},
      {"capacity":39,"eightd_has_key_dispenser":true,"electric_bike_surcharge_waiver":false,"external_id":"66db3708-0aca-11e7-82f6-3863bb44ef7c","has_kiosk":true,"lat":40.70277159,"lon":-73.99383605,"name":"Old Fulton St","region_id":71,"rental_methods":["KEY","CREDITCARD"],"rental_url":"http://app.citibikenyc.com/S6Lr/IBV092JufD?station_id=217","short_name":"4903.08","station_id":"217"}
  ]
  ```

6. Live status of an arbitrary CitiBike station:

* [GET /system/NYC/station/212](https://bikeshare.pythonanywhere.com/app/api/v1.0/system/NYC/station/212)

* JSON Responsee (dictionary): 
  ```json
  {
      "capacity":60,
      "eightd_has_available_keys":false,
      "eightd_has_key_dispenser":false,
      "electric_bike_surcharge_waiver":false,
      "external_id":"66db3606-0aca-11e7-82f6-3863bb44ef7c",
      "has_kiosk":true,
      "is_installed":1,
      "is_renting":1,
      "is_returning":1,
      "last_reported":1568992566,
      "last_updated":"Fri, 20 Sep 2019 15:16:59 GMT",
      "lat":40.74334935,
      "lon":-74.00681753,
      "name":"W 16 St & The High Line",
      "num_bikes_available":52,
      "num_bikes_disabled":0,
      "num_docks_available":8,
      "num_docks_disabled":0,
      "num_ebikes_available":0,
      "region_id":71,
      "rental_methods":["KEY","CREDITCARD"],
      "rental_url":"http://app.citibikenyc.com/S6Lr/IBV092JufD?station_id=212",
      "short_name":"6233.05",
      "station_id":"212",
      "ttl":10
  }
  ```
