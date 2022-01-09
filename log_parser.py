import argparse
import re
import json
from collections import defaultdict, Counter
import collections

parser = argparse.ArgumentParser(description='server log.log')
parser.add_argument('-f', dest='file', action='store', help='Full path to logfile')
args = parser.parse_args()

dict_ip = defaultdict(lambda: {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "HEAD": 0})
dict_count_get = {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "HEAD": 0}
d_ips = defaultdict(int)
d_time = defaultdict(int)
c = collections.Counter()

with open(args.file) as file:
    for index, line in enumerate(file.readlines()):
        try:
            ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line).group()
            method = re.search(r"\] \"(POST|GET|PUT|DELETE|HEAD)", line).groups()[0]
            time = re.search(r"\d{1,3} (\d{1,5})", line).groups()[0]
        except AttributeError:
            pass

        d_ips[ip] += 1
        #dict_ip[ip][method] += 1
        d_time[time] += 1
        top_ip = Counter(d_ips).most_common(10)
        dict_count_get[method] += 1
        time_x = time

        if index > 99:
            break

print("Всего запросов:", index+1)
print("Распределение запросов", json.dumps(dict_count_get, indent=4))
print("Top 10 ip:", json.dumps(top_ip))
