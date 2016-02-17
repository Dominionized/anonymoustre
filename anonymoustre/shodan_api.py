import shodan
import pprint
from api_key import SHODAN as SHODAN_KEY


pp = pprint.PrettyPrinter(indent=2)
api = shodan.Shodan(SHODAN_KEY)


def query_shodan_api(ips):
    results = []
    for ip in ips:
        print("patatedudebifu")
        try:
            results.append(api.host(ip))
        except shodan.APIError:
            results.append(None)
    return results

def get_shodan_score_delta(score_dict):
    raise NotImplementedError()
