# fbcrwal
gather facebook post message using graphAPI + python

Requirements & Procedure<br>
1. Facebook Graph API Token
2. Facebook Page Public Content Access
3. (if possible) Mange_pages & Publish_pages Access
4. Use my fbtest.py code and input data into excel
5. Use process.py code to analiyze the crawled result


참고 사이트 및 코드<br>
크롤링<br>
https://m.blog.naver.com/PostView.nhn?blogId=imsam77&logNo=221258133789&proxyReferer=https%3A%2F%2Fwww.google.com%2F<br>
크롤링 코드<br>
https://blog.naver.com/PostView.nhn?blogId=imsam77&logNo=221260229647&proxyReferer=https%3A%2F%2Fwww.google.com%2F<br>

# Example
부산에 있는 삼락생태공원과 대저생태공원의 페이스북 키워드를 수집하여 분석하였다.<br>
우선 페이스북 Graph API를 통하여 수집 데이터를 JSON으로 저장한다.<br>
그후 JSON에 있는 message를 엑셀로 정리하도록 프로그램을 설계한다.<br>
정리된 엑셀에서 텍스트 마이닝으로 형태소를 분석한다.<br>

## Procedure
![procedure](https://github.com/hansnam1105/fbcrwal/blob/master/example/ex1.png)

## Procedure2
![procedure2](https://github.com/hansnam1105/fbcrwal/blob/master/example/ex2.png)

## Result
![result](https://github.com/hansnam1105/fbcrwal/blob/master/example/ex3.png)
