import socket

FAIL_FACTOR = -50
DNSBL_LIST = [
    {'name': 'SORBS', 'hostname': 'spam.dnsbl.sorbs.net', 'codes': ['127.0.0.6']},
    {'name': 'Spamhaus', 'hostname': 'sbl.spamhaus.org', 'codes': ['127.0.0.2', '127.0.0.3']}]


def add_reverse_ip_bytes(ip):
    ip_adress = ip['ip']
    blocks = ip_adress.split('.')
    blocks.reverse()
    ip['reversed'] = '.'.join(blocks)
    return ip


def default_ip_map(ip):
    ip_map = {'ip': ip}
    ip_map['data'] = {}
    ip_map['failed'] = 0
    for dnsbl in DNSBL_LIST:
        dnsbl_name = dnsbl['name']
        ip_map['data'][dnsbl_name] = False
    return ip_map


def create_dns_request_uri(reversed_ip, dnsbl_hostname):
    return '.'.join([reversed_ip, dnsbl_hostname])


def dnsbl_request(ip, dnsbl):
    uri = create_dns_request_uri(ip['reversed'], dnsbl['hostname'])
    try:
        # print('Current URI is: {0}'.format(uri))
        response = socket.gethostbyname(uri)
        # print('Response for {0} on {1} is: {2}'.format(ip['ip'], dnsbl['name'], response))
        for response_code in dnsbl['codes']:
            if response_code in response:
                dnsbl_name = dnsbl['name']
                ip['data'][dnsbl_name] = True
                ip['failed'] += 1
    except socket.error:
        # print('An exception occured: {0}'.format(err))
        pass


def query_dnsbl_list(ips):
    ips_map = map(default_ip_map, ips)
    ips_map = map(add_reverse_ip_bytes, ips_map)
    for ip in ips_map:
        for dnsbl in DNSBL_LIST:
            dnsbl_request(ip, dnsbl)
    failed_count_list = map(lambda x: x['failed'], ips_map)
    return map(get_dnsbl_list_score_delta, failed_count_list)


def get_dnsbl_list_score_delta(failed_count):
    spam_score = failed_count * FAIL_FACTOR
    score = {'malware_score': 0,
             'phishing_score': 0,
             'unwanted_score': 0,
             'spam_score': spam_score}
    return score
