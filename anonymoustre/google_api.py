import api_key
from functools import reduce
import requests
from utils import assoc_default_scores, combine_scores, assoc_zero_scores


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

    print("Queried Google API. Got {0} status code".format(r.status_code))

    if r.status_code == 204:
        return assoc_zero_scores(ip_list)
    elif r.status_code == 200:
        return [get_google_score_delta(score_str) for score_str in r.text.split('\n')]


def get_google_score_delta(score_str):
    score = {}
    if "unwanted" in score_str:
        score["unwanted_score"] = -10
    elif "malware" in score_str:
        score["malware_score"] = -10
    elif "phishing" in score_str:
        score["phishing_score"] = -10
    return score
