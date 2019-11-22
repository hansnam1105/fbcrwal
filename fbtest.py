import json
import pandas as pd
import numpy as np
import facebook


token = '2418498638416310|3aba3f0a42a296a291a91837d4891922'
graph = facebook.GraphAPI(access_token=token, version="3.1")
pages_data = graph.request("/BusanCity?fields=access_token,feed.limit(500){message}")

with open("test.json", "w", encoding='utf-8') as f:
    f.write(json.dumps(pages_data, ensure_ascii=False, indent="\t"))

with open("test.json", "r", encoding='utf-8') as fp:
    test = json.load(fp)

test_string = []
for i in test['feed']['data']:
    if 'message' in i:
        if '대저생태공원' in i['message']:
            test_string.append(i['message'])
data = pd.DataFrame(test_string)
data.to_excel('test.xlsx')