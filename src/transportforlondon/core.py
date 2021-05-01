import logging

class TransportForLondon:

  LUAURL = "https://api.tfl.gov.uk/"

  def __init__(self):
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("New TransportForLondon instance created")
