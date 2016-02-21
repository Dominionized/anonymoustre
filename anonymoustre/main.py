from functools import reduce
import pprint
import time
import shodan
import requests
import api_key
from google_api import query_google_api
from shodan_api import query_shodan_api
from mxtoolbox_api import query_mxtoolbox_api
from dnsbl import query_dnsbl_list
from utils import assoc_default_scores, combine_scores


pp = pprint.PrettyPrinter(indent=2)


def main():
    start_time = time.time()

    # No more than 10 requests
    ips = get_bad_ips()[:5]
    scored_ips = assoc_default_scores(ips)

    shodan_scores = query_shodan_api(ips)
    google_scores = query_google_api(ips)
    dnsbl_scores = query_dnsbl_list(ips)
    # Limited number of requests... Be careful
    # mx_toolbox_scores = query_mxtoolbox_api(ips)

    results = reduce(combine_scores, [scored_ips, shodan_scores, google_scores, dnsbl_scores])
    pp.pprint(results)

    print("--------- %s seconds -------" % (time.time() - start_time))

    return results


def get_some_ips():
    req = requests.get("https://zeustracker.abuse.ch/blocklist.php?download=badips")
    return [line for line in req.text.split('\n') if line and line[0].isdigit()]


def get_bad_ips():
    with open("bad_ips.txt", "r") as file:
        ips = list(filter(lambda line: line != '', file.read().split("\n")))
    return ips


if __name__ == "__main__":
    main()
