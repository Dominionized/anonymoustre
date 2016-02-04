import shodan
import api_key

api = shodan.Shodan(api_key.API_KEY)
# Wrap the request in a try/ except block to catch errors
try:

    # Search Shodan
    results = api.search('apache')

    # Show the results
    print('Results found: %s' % results['total'])
    for result in results['matches']:
        print ('IP: %s' % result['ip_str'])
        print (result['data'])
        print ('')

except shodan.APIError as e:
    print('Error: %s' % e)
