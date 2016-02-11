import shodan
import api_key
import requests
import pprint
from functools import reduce


def main():
    api = shodan.Shodan(api_key.SHODAN)
    # Wrap the request in a try/ except block to catch errors
    try:
        # Search Shodan
        results = api.search('apache')

        # Show the results
        print('Results found: %s' % results['total'])
        for result in results['matches']:
            print('IP: %s' % result['ip_str'])
            print(result['data'])
            print('')

    except shodan.APIError as e:
        print('Error: %s' % e)


def query_google_api(ip_list):
    url = "https://sb-ssl.google.com/safebrowsing/api/lookup"
    url_params = {
        "client": "anonymoustre",
        "key": api_key.GOOGLE_SAFE_BROWSING,
        "appver": "0.0.1",
        "pver": "3.1"
    }
    req_body = str(len(ip_list)) + "\n" + reduce(lambda x, y: x+"\n"+y, ip_list)

    print(req_body)

    r = requests.post(url, params=url_params, data=req_body)

    print(r.status_code)
    print(r.text)

    if r.status_code == 204:
        return # TODO change this

def assoc_score(ip_list):
    return map(lambda ip: (ip, 100), ip_list)

if __name__ == "__main__":
    pprint(assoc_score(["192.168.1.1", "192.168.1.2", "192.168.0.43"]))
