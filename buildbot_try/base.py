import requests
import json

def tryclient():
    url = 'http://buildbot.sharmalabs.org:8020/api/v2/forceschedulers'
    r = requests.get(url)
    return json.loads(r.text)
