import requests
from datetime import datetime

HOSTNAME = open('docker_ip.cfg', 'r').read().strip()
PORT = 8080
STATS_INTERVAL = 1.0

print("Testing against host: {}".format(HOSTNAME))
print("Port being tested: {}".format(PORT))

def printstats(stats):
    for key in sorted(stats, key=int):
        print("{}\t{}".format(key,stats[key]))

# build a pre-prepared request object 
request_object = requests.Request('GET', 'http://{}:{}'.format(HOSTNAME,PORT)).prepare()

stats = {}
lasttime = datetime.now()
try:
    while True:
        delta = datetime.now() - lasttime
        if delta.seconds > STATS_INTERVAL:
            lasttime = datetime.now()
            # generate per-interval stats
            print("Stats:")
            printstats(stats)
            stats = {}
        else:
            with requests.Session() as s:
                try:
                    # do the request, work out the stats
                    ret = s.send(request_object)
                    if ret.status_code == 200:
                        ret = ret.text.strip()
                        stats[ret] = stats.get(ret,1)+1
                # handle when a server drops
                except requests.exceptions.ConnectionError:
                    pass
except KeyboardInterrupt:
    print("Quitting, final stats:")
    printstats(stats)
