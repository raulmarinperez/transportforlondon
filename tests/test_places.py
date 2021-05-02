from transportforlondon.places import Places
import argparse
import logging
import pprint
import sys
import os

# Auxiliary functions
#
def info_charge_connectors(places_service):
  info_charge_connectors = places_service.info_charge_connectors()

  if info_charge_connectors!=None:
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(info_charge_connectors)
  else:
    print("The Places service didn't return any data.")

# Setting up debuging level and debug file with environment variables
#
debug_level = os.environ.get('TFL_DEBUGLEVEL',logging.WARN)
debug_file = os.environ.get('TFL_DEBUGFILE')

if debug_file==None:
  logging.basicConfig(level=debug_level)
else:
  logging.basicConfig(filename=debug_file, filemode='w', level=debug_level)

parser = argparse.ArgumentParser()
parser.add_argument("action", choices=['info_charge_connectors'],
                    help="what is going to be requested to the Unified API service")
args = parser.parse_args()

places_service = Places()

# Action dispatching if credentials logged the client into the service
#
if args.action == "info_charge_connectors":
  logging.debug("asking for info of all charge connectors")
  info_charge_connectors(places_service)
