#!/usr/bin/env python
########### Python 2.7 #############
import httplib, urllib, base64
 
headers = {
    # Basic Authorization Sample
    # 'Authorization': 'Basic %s' % base64.encodestring('{username}:{password}'),
}
 
params = urllib.urlencode({
    'api_key': 'kfgpmgvfgacx98de9q3xazww',
})
 
try:
    conn = httplib.HTTPSConnection('api.wmata.com')
    conn.request("GET", "/StationPrediction.svc/json/GetPrediction/All?%s" % params, "", headers)
    response = conn.getresponse()
    data = json.load(response)
    for item in data['Trains']:
        if item['LocationName'] == "Ballston-MU" and item['Line'] == "OR":
            print '\033[1m' + item['LocationName'] + '\033[0m'
            print 'Orange Line ({}) Train to {}'.format(item['Line'], item['Destination'])
            print 'Arrives in {} Minutes'.format(item['Min'])
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
 
