from functools import reduce
import pprint
import shodan
import requests
import api_key
from google_api import query_google_api
from shodan_api import query_shodan_api


pp = pprint.PrettyPrinter(indent=2)


def main():
    ips = get_some_ips()
    goo = query_google_api(ips)
    pp.pprint(query_shodan_api(ips))
    return goo


def get_some_ips():
    req = requests.get("https://zeustracker.abuse.ch/blocklist.php?download=badips")
    return [line for line in req.text.split('\n') if line and line[0].isdigit()]


def get_bad_ips():
    with open("bad_ips.txt", "r") as file:
        ips = list(filter(lambda line: line != '', file.read().split("\n")))
    return ips


if __name__ == "__main__":
    main()
