import utils
import requests
from api_key import MX_TOOL_BOX

LOOKUP_URI = 'https://mxtoolbox.com/api/v1/lookup/'
FAIL_FACTOR = -15


def query_mxtoolbox_api(ips):
    # This could be done with Pool().map
    # to get faster results.
    toolbox_command = 'blacklist'
    uri_template = LOOKUP_URI + toolbox_command + '/'
    responses = []
    for ip in ips:
        if not utils.validate_IP(ip):
            raise ValueError('Invalid IP syntax')
        uri = uri_template + ip
        headers = {'Authorization': MX_TOOL_BOX}
        response = requests.get(uri, headers=headers)
        response.raise_for_status()
        print("MXToolBox's API queried for adress {0}. Got status code: {1}"
              .format(ip, response.status_code))
        responses.append(response.json()['Failed'])
    return map(get_mxtoolbox_score_delta, responses)


def get_mxtoolbox_score_delta(failures):
    spam_score = len(failures) * FAIL_FACTOR
    score = {'malware_score': 0,
             'phishing_score': 0,
             'unwanted_score': 0,
             'spam_score': spam_score}
    return score
