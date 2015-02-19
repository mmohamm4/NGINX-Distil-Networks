#!/usr/bin/env python
import urllib2
import json
    
data = json.load(urllib2.urlopen('https://api.wmata.com/StationPrediction.svc/json/GetPrediction/All?api_key=kfgpmgvfgacx98de9q3xazww'))

for item in data['Trains']:
    if item['LocationName'] == "Ballston-MU" and item['Line'] == "OR":
        print '\033[1m' + item['LocationName'] + '\033[0m'
        print 'Orange Line ({}) Train to {}'.format(item['Line'], item['Destination'])
        print 'Arrives in {} Minutes'.format(item['Min'])
