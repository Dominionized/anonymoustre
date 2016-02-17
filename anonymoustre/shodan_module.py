import shodan as shodanapi
import pprint
from api_key import SHODAN as SHODAN_KEY


APIError = shodanapi.APIError
pp = pprint.PrettyPrinter(indent=2)
shodan = shodanapi.Shodan(SHODAN_KEY)


def get_hosts_data(ips):
    results = []
    for ip in ips:
        try:
            results.append(shodan.host(ip))
        except shodan.APIError:
            results.append(None)
    return results
