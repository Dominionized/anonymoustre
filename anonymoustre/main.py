import shodan
import api_key
import requests
import pprint
from functools import reduce


pp = pprint.PrettyPrinter(indent=2)

def main():
    ips = get_some_ips()
    google = query_google_api(ips)

def get_some_ips():
    req = requests.get("https://zeustracker.abuse.ch/blocklist.php?download=badips")
    return [line for line in req.text.split('\n') if line and line[0].isdigit()]

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

    scored_ip_list = assoc_default_score(ip_list)

    if r.status_code == 204:
        return scored_ip_list
    elif r.status_code == 200:
        return combine_scores(scored_ip_list, [get_score_delta(score_str) for score_str in r.text.split('\n')])

def get_score_delta(score_str):
    score = {}
    if "unwanted" in score_str:
        score["unwanted_score"] = -10
    elif "malware_score" in score_str:
        score["malware_score"] = -10
    elif "phishing_score" in score_str:
        score["phishing_score"] = -10
    return score

def assoc_default_score(ip_list):
    return list(map(lambda ip: {
        "ip": ip,
        "malware_score": 100,
        "phishing_score": 100,
        "unwanted_score": 100 }, ip_list))

def combine_scores(scores1, scores2):
    return [combine_score(e1, e2) for e1,e2 in zip(scores1, scores2)]

def combine_score(beg_score, score_to_add):
    combined = beg_score
    for key in score_to_add:
        if key in combined:
            combined[key] += score_to_add[key]
    return combined

if __name__ == "__main__":
    main()