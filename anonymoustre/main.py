import shodan
import api_key
import requests
import pprint
from functools import reduce


pp = pprint.PrettyPrinter(indent=2)

def main():
    ips = get_some_ips()
    query_google_api(ips)
    pp.pprint(ips)
    #pp.pprint(query_google_api([res['ip_str'] for res in results['matches']]))

def query_google_api(ip_list):
    url = "https://sb-ssl.google.com/safebrowsing/api/lookup"
    url_params = {
        "client": "anonymoustre",
        "key": api_key.GOOGLE_SAFE_BROWSING,
        "appver": "0.0.1",
        "pver": "3.1"
    }
    req_body = str(len(ip_list)) + "\n" + reduce(lambda x, y: x+"\n"+y, ip_list)

    r = requests.post(url, params=url_params, data=req_body)

    print(r.status_code)
    print(r.text)

    if r.status_code == 204:
        return [{"unwanted_score": 0, "malware_score": 0, "phishing_score": 0} for i in range(len(ip_list))]

def assoc_score(ip_list):
    return list(map(lambda ip: {
        "ip": ip,
        "malware_score": 100,
        "phishing_score": 100,
        "unwanted_score": 100 }, ip_list))

def get_some_ips():
    req = requests.get("https://zeustracker.abuse.ch/blocklist.php?download=badips")
    return [line for line in req.text.split('\n') if line and line[0].isdigit()]

def combine_scores(scores1, scores2):
    for e1, e2 in zip(scores1, scores2):
        print(e1)
        print(e2)
        # TODO : change this

if __name__ == "__main__":
    main()
