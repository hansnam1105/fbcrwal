import json
from pprint import pprint

import facebook


token = '2418498638416310|3aba3f0a42a296a291a91837d4891922'
graph = facebook.GraphAPI(access_token=token, version="3.1")
pages_data = graph.request("/welovebusan?fields=access_token,feed.limit(300){message}")

with open("test.json", "w", encoding='utf-8') as f:
    f.write(json.dumps(pages_data, ensure_ascii=False, indent="\t"))

with open("test.json", "r", encoding='utf-8') as fp:
    test = json.load(fp)

test_string = []
for i in test['feed']['data']:
    if 'message' in i:
        if '대저생태공원' in i['message']:
            test_string = i['message']
            print(test_string)

'''for i in test['feed']['data']:
    if "대저생태공원" in test['feed']['data'][i]['message']:
        test_string = test['feed']['data'][i]['message']'''