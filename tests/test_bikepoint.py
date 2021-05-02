from transportforlondon.bikepoint import BikePoint
import argparse
import logging
import pprint
import sys
import os

# Auxiliary functions
#
def info_bikepoint_locations(bikepoint_service):
  info_bikepoint_locations = bikepoint_service.info_bikepoint_locations()

  if info_bikepoint_locations!=None:
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(info_bikepoint_locations)
  else:
    print("The BikePoint service didn't return any data.")

def info_bikepoint(bikepoint_service, bikepoint_id):
  info_bikepoint = bikepoint_service.info_bikepoint(bikepoint_id)

  if info_bikepoint!=None:
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(info_bikepoint)
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
parser.add_argument("action", choices=['info_bikepoint_locations', 'info_bikepoint'],
                    help="what is going to be requested to the Unified API service")
parser.add_argument("-bid", "--bikepoint_id",
                    help="bikepoint identifier for action 'info_bikepoint'")
args = parser.parse_args()

bikepoint_service = BikePoint()

# Action dispatching if credentials logged the client into the service
#
if args.action == "info_bikepoint_locations":
  logging.debug("asking for all bikepoint locations")
  info_bikepoint_locations(bikepoint_service)
elif args.action == "info_bikepoint":
  logging.debug("asking for info about bikepoint '%s'" % args.bikepoint_id)
  info_bikepoint(bikepoint_service, args.bikepoint_id)
