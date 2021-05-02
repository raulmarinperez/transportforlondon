from transportforlondon.core import TransportForLondon
import logging
import requests

class BusService(TransportForLondon):
  '''APIs relating to the Bus service. It allows getting bus lines and
     theis status.
  '''
  def __init__(self):
    TransportForLondon.__init__(self)

  def info_bus_lines(self):
    '''Gets lines that serve the given modes.

            Parameters:
                    None

            Returns:
                    Array of JSON documents with the bus lines.
                    or None if there was an error.
                    (See https://api-portal.tfl.gov.uk/api-details#api=ReleasedUnifiedAPIProd&operation=Line_GetByMode)
    '''
    url = "%s/Line/Mode/bus" % self.LUAURL
    resp = requests.get(url)

    if resp.status_code == 200:
      logging.debug("Bus lines received: %s" % resp.json())
      return resp.json()

    logging.error("Unable to retrieve the list of bus lines with code '%s' and message: %s" %
                  (resp.status_code, resp.reason))
    return None

  def status_bus_lines(self):
    '''Gets the line status of for all bus lines.

            Parameters:
                    None

            Returns:
                    Array of JSON documents with the status of bus lines
                    or None if there was an error.
                    (See https://api-portal.tfl.gov.uk/api-details#api=ReleasedUnifiedAPIProd&operation=Line_StatusByMode)
    '''
    url = "%s/Line/Mode/bus/Status" % self.LUAURL
    resp = requests.get(url)

    if resp.status_code == 200:
      logging.debug("Status of bus lines: %s" % resp.json())
      return resp.json()

    logging.error("Unable to retrieve status of bus lines with code '%s' and message: %s" %
                  (resp.status_code, resp.reason))
    return None


  def status_bus_line(self, bus_line_id):
    '''Gets the line status of for given line id.

            Parameters:
                    None

            Returns:
                    Array of JSON documents with the status of a bus lines.
                    or None if there was an error.
                    (See https://api-portal.tfl.gov.uk/api-details#api=ReleasedUnifiedAPIProd&operation=Line_StatusByIds)
    '''
    url = "%s/Line/%s/Status" % (self.LUAURL,bus_line_id)
    resp = requests.get(url)

    if resp.status_code == 200:
      logging.debug("Status of bus line '%s': %s" % (resp.json(),bus_line_id))
      return resp.json()

    logging.error("Unable to retrieve status of bus line '%s' with code '%s' and message: %s" %
                  (bus_line_id, resp.status_code, resp.reason))
    return None

