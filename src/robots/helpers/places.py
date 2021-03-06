import os
import json
import logging; logger = logging.getLogger("robot." + __name__)

#hack that tries to find out the current prefix and then the data directory
DATA_DIR = os.path.abspath(__file__).split('lib')[0] + '/share/pyrobots/'

source = DATA_DIR + 'appart_places.json'

_places = None

def places():
    global _places
    if not _places:
        logger.info("Reading symbolic places from " + source)
        f = open(source,'r')
        json_data=f.read()
        _places = json.loads(json_data)
    return _places

