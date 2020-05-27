import requests
import json
import sys

endpoint = "https://slack.com/api/conversations.history"

def getChannelContent():
    response = requests.get(
        '%s' % (endpoint +"?channel="+channel+"&limit=1000"),
        headers={'Authorization': 'Bearer %s' % token, 
            "Content-Type": "application/x-www-form-urelencoded"}
    )
    result = json.loads(response.text)
    cnt = 0

    for i in result['messages']:
        if '?' in i['text']:
            cnt += 1
    print(cnt)
        
if __name__ == '__main__':
    channel = sys.argv[1]
    token = sys.argv[2]
    getChannelContent()
