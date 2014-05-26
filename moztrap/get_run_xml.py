#!/usr/bin/python

import requests, json, codecs

jsonurl='https://moztrap.mozilla.org/api/v1/runcaseversion/?format=json&run=4169&limit='

url='https://moztrap.mozilla.org/api/v1/runcaseversion/?format=xml&run=4169&limit='
limit=20
offset=0
res = requests.get(jsonurl + str(limit)).json()
size = res['meta']['total_count']
sn = 1
limit=50
for offset in xrange(0, size, limit):
    tc = codecs.open('testcase'+ str(sn) +'.data', 'w', 'utf-8')
    res = requests.get(url + str(limit) + '&offset=' + str(offset))
    tc.write(res.text)
    tc.close()
