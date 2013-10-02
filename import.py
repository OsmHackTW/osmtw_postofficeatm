#!/usr/bin/python3
# Rex Tsai <chihchun@kalug.linux.org.tw>

import OsmApi
import csv
import sys
from pprint import pprint
from subprocess import call

delta = 0.002
readonly = True
debug = True

osm = OsmApi.OsmApi(passwordfile="passwd", appid = 'RexBot', debug=debug, changesetauto=False)

if (readonly is not True):
    print ("changeset id %d" % (osm.ChangesetCreate({u"comment": u"中華郵政 ATM 資訊自動修正"})), file=sys.stderr)

with open('post_atm_location.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        match = list()
        lon = float(row[6])
        lat = float(row[7])
        data = osm.Map(lon-delta, lat-delta, lon+delta, lat+delta);
        for i in data:
           if (i['data']['tag'] and 'amenity' in i['data']['tag'] and i['data']['tag']['amenity'] == 'atm'):
                match.append(i)

        if(len(match) == 1):
            node = match[0]['data']
            node['tag']['operator'] = '中華郵政'
            node['tag']['currency:twd'] = 'yes'
            node['tag']['description'] = row[3]
            node['tag']['description'] = "%s%s%s%s%s%s" % (row[3],row[12],row[8],row[9],row[10],row[11])
            node['tag']['address'] = row[0]+row[1]+row[5]
            node['tag']['phone'] = row[4].replace('(0', '+886-').replace(')','-').replace('轉', 'p')
             
            pprint(node)
            # call(("/usr/bin/firefox http://www.openstreetmap.org/#map=19/%f/%f" % (lat, lon)).split())
            if (not readonly):
                osm.NodeUpdate(node)

if (not readonly):
    osm.ChangesetClose()

