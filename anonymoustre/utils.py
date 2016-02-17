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
