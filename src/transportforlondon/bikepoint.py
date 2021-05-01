from transportforlondon.core import TransportForLondon
import logging
import requests

class BikePoint(TransportForLondon):
  '''APIs relating to BikePoint and similar services. It will provide
     information about available docks, busy docks and damaged docks.
  '''
  def __init__(self):
    TransportForLondon.__init__(self)

  def all_bikepoint_locations(self):
    '''Gets all bike point locations. The Place object has an addtionalProperties 
       array which contains the nbBikes, nbDocks and nbSpaces numbers which give 
       the status of the BikePoint. A mismatch in these numbers 
       i.e. nbDocks - (nbBikes + nbSpaces) != 0 indicates broken docks.

            Parameters:
                    None

            Returns:
                    Array of JSON documents with information about the bike points
                    or None if there was an error.
                    (See https://api-portal.tfl.gov.uk/api-details#api=ReleasedUnifiedAPIProd&operation=BikePoint_GetAll)
    '''
    url = "%s/BikePoint" % self.LUAURL
    resp = requests.get(url)

    if resp.status_code == 200:
      logging.debug("Info of bikepoint locations: %s" % resp.json())
      return resp.json()

    logging.error("Unable to retrieve the list of bikepoint locations with code '%s' and message: %s" %
                  (resp.status_code, resp.reason))
    return None

