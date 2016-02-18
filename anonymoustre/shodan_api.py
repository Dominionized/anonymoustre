import shodan
import pprint
from nested_lookup import nested_lookup
from multiprocessing import Pool, TimeoutError
from api_key import SHODAN as SHODAN_KEY
from utils import combine_scores


pp = pprint.PrettyPrinter(indent=2)
api = shodan.Shodan(SHODAN_KEY)


def query_shodan_api(ips):
    pool = Pool(processes=48)
    return list(pool.map(get_shodan_score_delta, ips))

def get_shodan_score_delta(ip):
    score = {"malware_score" : 0, "phishing_score" : 0, "unwanted_score" : 0, "unsecure_score": 0}
    try:
        response = api.host(ip)
        score['unsecure_score'] = -10 * list(nested_lookup('expired', response)).count(True)
        return score
    except shodan.APIError:
        return score
