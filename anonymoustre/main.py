import shodan
import api_key
import requests


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


def query_google_api():

    url_params = {
        "client": "anonymoustre",
        "key": api_key.GOOGLE_SAFE_BROWSING,
        "appver": "0.0.1",
        "pver": "3.1"
    }

    req_body = "2\nhttp://sourceforge.net/\nhttp://google.com/"

    r = requests.post("https://sb-ssl.google.com/safebrowsing/api/lookup",
                                params=url_params,
                                data=req_body)
    print(r.url)
    print(r.headers)
    print(r.status_code)
    print(r.text)


if __name__ == "__main__":
    query_google_api()
