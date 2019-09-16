bikeshare-demo-app
------------------

A json api for polling live Bikeshare feeds, demonstrating a simple [bikeshare-client-python](https://github.com/jakehadar/bikeshare-client-python) use-case.

The API spec is annotated in [app.py](https://github.com/jakehadar/bikeshare-demo-app/blob/master/app.py)


REST example
------------

Query all systems:

* [GET /systems](https://bikeshare.pythonanywhere.com/app/api/v1.0/systems)

Select CitiBike (NYC):

* [GET /system/NYC](https://bikeshare.pythonanywhere.com/app/api/v1.0/system/NYC)

List of feeds provided by CitiBike:

* [GET /system/NYC/feeds](https://bikeshare.pythonanywhere.com/app/api/v1.0/system/NYC/feeds)

CitiBike system alerts:

* [GET /system/NYC/feed/system_alerts](https://bikeshare.pythonanywhere.com/app/api/v1.0/system/NYC/feed/system_alerts)

All CitiBike stations:

* [GET /system/NYC/stations](https://bikeshare.pythonanywhere.com/app/api/v1.0/system/NYC/stations)

Live status of an arbitrary CitiBike station:

* [GET /system/NYC/station/212](https://bikeshare.pythonanywhere.com/app/api/v1.0/system/NYC/station/212)
