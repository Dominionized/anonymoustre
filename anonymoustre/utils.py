from IPy import IP

DEFAULT_SCORE = 100


def assoc_default_score(ip_list):
    return list(map(assoc_single_default_score, ip_list))

def assoc_single_default_score(ip):
    return {
        "ip": ip,
        "malware_score": DEFAULT_SCORE,
        "phishing_score": DEFAULT_SCORE,
        "unwanted_score": DEFAULT_SCORE,
        "unsecure_score": DEFAULT_SCORE,
        "spam_score": DEFAULT_SCORE}

def assoc_single_zero_score(ip):
    return {
        "ip": ip,
        "malware_score": 0,
        "phishing_score": 0,
        "unwanted_score": 0,
        "unsecure_score": 0,
        "spam_score": 0}

zero_score = {
    "malware_score": 0,
    "phishing_score": 0,
    "unwanted_score": 0,
    "unsecure_score": 0,
    "spam_score": 0}

def combine_scores(scores1, scores2):
    return [combine_score(e1, e2) for e1, e2 in zip(scores1, scores2)]


def combine_score(beg_score, score_to_add):
    print("Combining")
    print(beg_score)
    print(score_to_add)
    print("-----------------------------------")
    combined = beg_score
    for key in score_to_add:
        if key in combined:
            combined[key] += score_to_add[key]
    return combined


def validate_IP(ip):
    try:
        IP(ip)
    except ValueError:
        return False
    return True
