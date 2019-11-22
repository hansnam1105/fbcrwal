import json
import pandas as pd
import numpy as np
import facebook
import openpyxl


token = '2418498638416310|3aba3f0a42a296a291a91837d4891922'
graph = facebook.GraphAPI(access_token=token, version="3.1")
wb = openpyxl.load_workbook('samlak.xlsx')

sheet1 = wb.active

#부산 광역시
#pages_data = graph.request("/BusanCity?fields=access_token,feed.limit(500){message,created_time}")
#부산에서 뭐 하지
#pages_data = graph.request("/all.about.pusan?fields=access_token,feed.limit(300){message,created_time}")
#부산플래닛
#pages_data = graph.request("/busanplanet?fields=access_token,feed.limit(500){message,created_time}")
#부산 아입니꺼
#pages_data = graph.request("/welovebusan?fields=access_token,feed.limit(300){message,created_time}")
#부산광역시 강서구청
#pages_data = graph.request("/bsgangseo?fields=access_token,feed.limit(200){message,created_time}")
#부산광역시 사상구청
#pages_data = graph.request("/funbssasang?fields=access_token,feed.limit(300){message,created_time}")
#창원여자
#pages_data = graph.request("/changwonwomans?fields=access_token,feed.limit(300){message,created_time}")
#부산에서 살면 꼭 가봐야하는곳들
#pages_data = graph.request("/busanggok?fields=access_token,feed.limit(300){message,created_time}")
# -----------------------------
#여행 다녀왔습니다
#pages_data = graph.request("/travelmenu1?fields=access_token,feed.limit(300){message,created_time}")
#부산이모
#pages_data = graph.request("/bsevent?fields=access_token,feed.limit(400){message,created_time}")
#직접가본 데이트코스
#pages_data = graph.request("/gogoevent?fields=access_token,feed.limit(500){message,created_time}")
#부산소식
#pages_data = graph.request("/busansochic?fields=access_token,feed.limit(300){message,created_time}")
#부산 놀자
#pages_data = graph.request("/busansomang?fields=access_token,feed.limit(200){message,created_time}")
#부산 대신 전해드립니다
pages_data = graph.request("/busan1414?fields=access_token,feed.limit(500){message,created_time}")

with open("test.json", "w", encoding='utf-8') as f:
    f.write(json.dumps(pages_data, ensure_ascii=False, indent="\t"))

with open("test.json", "r", encoding='utf-8') as fp:
    test = json.load(fp)

test_string = []
for i in test['feed']['data']:
    if 'message' in i:
        if '삼락생태공원' in i['message']:
            test_string.append(i['message'])
            sheet1.append([i['message']])
            print("1")

wb.save('samlak.xlsx')