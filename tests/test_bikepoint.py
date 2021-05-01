from transportforlondon.bikepoint import BikePoint
import argparse
import logging
import pprint
import sys
import os

# Auxiliary functions
#
def all_bikepoint_locations(bikepoint_service):
  all_bikepoint_locations = bikepoint_service.all_bikepoint_locations()

  if all_bikepoint_locations!=None:
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(all_bikepoint_locations)
  else:
    print("The BikePoint service didn't return any data.")

# Setting up debuging level and debug file with environment variables
#
debug_level = os.environ.get('TFL_DEBUGLEVEL',logging.WARN)
debug_file = os.environ.get('TFL_DEBUGFILE')

if debug_file==None:
  logging.basicConfig(level=debug_level)
else:
  logging.basicConfig(filename=debug_file, filemode='w', level=debug_level)

parser = argparse.ArgumentParser()
parser.add_argument("action", choices=['all_bikepoint_locations'],
                    help="what is going to be requested to the Unified API service")
parser.add_argument("-sid", "--bike_station_id",
                    help="bike station identifier for action 'info_bike_station'")
parser.add_argument("-bid", "--bike_id",
                    help="bike identifier for action 'info_bike'")
args = parser.parse_args()

bikepoint_service = BikePoint()

# Action dispatching if credentials logged the client into the service
#
if args.action == "all_bikepoint_locations":
  logging.debug("asking for all bikepoint locations")
  all_bikepoint_locations(bikepoint_service)
