import argparse
import re
import json
from collections import defaultdict
# from collections import Counter

parser = argparse.ArgumentParser(description='server log.log')
parser.add_argument('-f', dest='file', action='store', help='Full path to logfile')
args = parser.parse_args()

dict_ip = defaultdict(lambda: {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "HEAD": 0})

with open(args.file) as file:
    for index, line in enumerate(file.readlines()):
        try:
            ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line).group()
            method = re.search(r"\] \"(POST|GET|PUT|DELETE|HEAD)", line).groups()[0]
        except AttributeError:
            pass

        dict_ip[ip][method] += 1

        if index > 99:
            break

#print(dict_ip)
print(json.dumps(dict_ip, indent=4))
