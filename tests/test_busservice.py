from transportforlondon.busservice import BusService
import argparse
import logging
import pprint
import sys
import os

# Auxiliary functions
#
def info_bus_lines(bus_service):
  info_bus_lines = bus_service.info_bus_lines()

  if info_bus_lines!=None:
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(info_bus_lines)
  else:
    print("The bus service didn't return any data.")

def status_bus_lines(bus_service):
  status_bus_lines = bus_service.status_bus_lines()

  if status_bus_lines!=None:
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(status_bus_lines)
  else:
    print("The bus service didn't return any data.")

def status_bus_line(bus_service, bus_line_id):
  status_bus_line = bus_service.status_bus_line(bus_line_id)

  if status_bus_line!=None:
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(status_bus_line)
  else:
    print("The bus service didn't return any data.")

# Setting up debuging level and debug file with environment variables
#
debug_level = os.environ.get('TFL_DEBUGLEVEL',logging.WARN)
debug_file = os.environ.get('TFL_DEBUGFILE')

if debug_file==None:
  logging.basicConfig(level=debug_level)
else:
  logging.basicConfig(filename=debug_file, filemode='w', level=debug_level)

parser = argparse.ArgumentParser()
parser.add_argument("action", choices=['info_bus_lines', 'status_bus_lines','status_bus_line'],
                    help="what is going to be requested to the Unified API service")
parser.add_argument("-bid", "--bus_line_id",
                    help="bus line identifier for action 'status_bus_line'")
args = parser.parse_args()

bus_service = BusService()

# Action dispatching if credentials logged the client into the service
#
if args.action == "info_bus_lines":
  logging.debug("asking for all bus lines")
  info_bus_lines(bus_service)
elif args.action == "status_bus_lines":
  logging.debug("asking for status of all bus lines")
  status_bus_lines(bus_service)
elif args.action == "status_bus_line":
  logging.debug("asking for status of bus line '%s'" % args.bus_line_id)
  status_bus_line(bus_service, args.bus_line_id)
