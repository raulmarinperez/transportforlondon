from transportforlondon.core import TransportForLondon
import logging
import requests

class Places(TransportForLondon):
  '''APIs relating to Place and similar services. It will provide
     information about places like ChargeConnectors.
  '''
  def __init__(self):
    TransportForLondon.__init__(self)

  def info_charge_connectors(self):
    '''Gets all places of a given type

            Parameters:
                    None

            Returns:
                    Array of JSON documents with information about charge connectors.
                    or None if there was an error.
                    (See https://api-portal.tfl.gov.uk/api-details#api=ReleasedUnifiedAPIProd&operation=Place_GetByType)
    '''
    url = "%s/Place/Type/ChargeConnector" % self.LUAURL
    resp = requests.get(url)

    if resp.status_code == 200:
      logging.debug("Info of charge connectors: %s" % resp.json())
      return resp.json()

    logging.error("Unable to retrieve info of charge connectors with code '%s' and message: %s" %
                  (resp.status_code, resp.reason))
    return None
