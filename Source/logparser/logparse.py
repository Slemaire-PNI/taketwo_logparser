import os
from itertools import chain
import math
import re

groupings = {
'requester_ip' : 0,
'statcode' : 8,
'referrer' : 10,
}

def calculate_percent(dict):
    dict_pct = {}
    total = sum(dict.values())
    for key, item in dict.items():
        pct = round((item * 100.0 / total), 2)
        dict_pct.update ( {key : pct } )
    return {k: str(v) + "%" for k, v in sorted(dict_pct.items(), key = lambda item: item[1], reverse=True)}

def parse():
    filename = os.environ['LOGFILE']
    requester_ip_map = {}
    statcode_map = {}
    referrer_map = {}

    if filename:
        files = [filename]
    else:
        files = os.listdir('/app/logs')

    for file in files:
        for line in open('/app/logs/' + file, "r").readlines():
            elements = line.split(' ')
            for group, index in groupings.items():

                key = elements[index]
                dict = eval(group + '_map')

                if key in dict:
                    dict[key] += 1
                else:
                    dict[key] = 1

    return {
        "UniqueIpCount": len(requester_ip_map),
        "IpRequestMap": requester_ip_map,
        "HttpCodeDist": calculate_percent(statcode_map),
        "Top5Referrers": sorted(referrer_map, key=referrer_map.get, reverse=True)[:5],
    }
