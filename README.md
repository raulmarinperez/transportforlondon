# Python wrapper for the Unified API of the Transport for London
This repo contains a Python library with some classes to easily access the [Unified API of the Transport for London](https://api-portal.tfl.gov.uk/api-details#api=ReleasedUnifiedAPIProd) which allows the access to the **BikePoints**, **Bus Lines** and **Places** services among others. These services are part of the [public TfL open data](https://api-portal.tfl.gov.uk/) platform.

In addition to the Python wrapper **some test applications are included**; this will help you know how everything works and, on top of that, you can use it to interact with the service. No credentials are needed to use the services covered at the moment.

The following are the requirements needed to make it work:

- **Python 3** (3.7.3+)

This Python library has been successfully tested with [OSBDET S21R1](https://github.com/raulmarinperez/osbdet/tree/vs21r1) on a Debian 10 x64 host.

Remember to add the library to the **PYTHONPATH environment variable** if you want to use it from your code or if you want to run the tests Python scripts; you can do so by running the following line within the folder where the repo was cloned:

```
$ export PYTHONPATH=$PYTHONPATH:`pwd`
```
If you want to persist this environment variable, **add it to your user's profile** and it'll be created everytime you log into your computer.

## BikePoint
The `BikePoint` class allows you to leverage information about bike point locations in the great city of London; this class wrapps the [BikePoint API](https://api-portal.tfl.gov.uk/api-details#api=BikePoint), although not all the functions/webmethods are wrapped.

The following are the functions/webmethods wrapped at the moment:

- **info_bikepoint_locations() -** Gets all bike point locations. The Place object has an addtionalProperties array which contains the nbBikes, nbDocks and nbSpaces numbers which givethe status of the BikePoint. A mismatch in these numbers i.e. nbDocks - (nbBikes + nbSpaces) != 0 indicates broken docks.
- **info_bikepoint(bikepoint_id) -** Gets the bike point with the given id.

`test_bikepoint.py` let you test this service easily; no credentials are needed. `test_bikepoint.py -h` will give you all the details on how to run it:

```
$ python3 tests/test_bikepoint.py -h
usage: test_bikepoint.py [-h] [-bid BIKEPOINT_ID]
                         {info_bikepoint_locations,info_bikepoint}

positional arguments:
  {info_bikepoint_locations,info_bikepoint}
                        what is going to be requested to the Unified API
                        service

optional arguments:
  -h, --help            show this help message and exit
  -bid BIKEPOINT_ID, --bikepoint_id BIKEPOINT_ID
                        bikepoint identifier for action 'info_bikepoint'
```

## BusService
The `BusService` class allows you to leverage information about bus lines in the great city of London; this class wrapps the [Line API](https://api-portal.tfl.gov.uk/api-details#api=Line), although not all the functions/webmethods are wrapped.

The following are the functions/webmethods wrapped at the moment:

- **info_bus_lines() -** Gets lines that serve the given modes.
- **status_bus_lines() -** Gets the line status of for all bus lines.
- **status_bus_line(bus_line_id) -** Gets the line status of for given line id.

`test_busservice.py` let you test this service easily; no credentials are needed. `test_busservice.py -h` will give you all the details on how to run it:

```
$ python3 tests/test_busservice.py -h
usage: test_busservice.py [-h] [-bid BUS_LINE_ID]
                          {info_bus_lines,status_bus_lines,status_bus_line}

positional arguments:
  {info_bus_lines,status_bus_lines,status_bus_line}
                        what is going to be requested to the Unified API
                        service

optional arguments:
  -h, --help            show this help message and exit
  -bid BUS_LINE_ID, --bus_line_id BUS_LINE_ID
                        bus line identifier for action 'status_bus_line'
```

## Places
The `Places` class allows you to leverage information about places in the great city of London; this class wrapps the [Place API](https://api-portal.tfl.gov.uk/api-details#api=Place), although not all the functions/webmethods are wrapped. Only ChargeStation and ChargeConnector places are considered at the moment.

The following are the functions/webmethods wrapped at the moment:

- **info_charge_connectors() -** Gets all available charge connectors.
- **info_charge_stations() -** Gets all available charge stations.

`test_places.py` let you test this service easily; no credentials are needed. `test_places.py -h` will give you all the details on how to run it:

```
$ python3 tests/test_places.py -h
usage: test_places.py [-h] {info_charge_connectors,info_charge_stations}

positional arguments:
  {info_charge_connectors,info_charge_stations}
                        what is going to be requested to the Unified API
                        service

optional arguments:
  -h, --help            show this help message and exit
```

## Changelog
- **v0.1 (20210502) -** initial release.
