import utils
import requests
from api_key import MX_TOOL_BOX

LOOKUP_URI = 'https://mxtoolbox.com/api/v1/lookup/'


class MXToolBox:

    def __init__(self, key):
        if key:
            self.key = key
        else:
            self.key = MX_TOOL_BOX

    def get_blacklist_data_from_ip(self, ip):
        if not utils.validate_IP(ip):
            raise ValueError('Invalid IP syntax')
        toolbox_command = 'blacklist'
        parsed_ip = LOOKUP_URI + toolbox_command + '/' + ip
        response = requests.get(parsed_ip)
        response.raise_for_status()
        return response.JSON()
