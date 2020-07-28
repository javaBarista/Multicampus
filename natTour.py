import urllib.request
import datetime
import time
import json
import pandas

def get_request_url(url, enc='utf-8'):
    url = url if url.find("http") != -1 else "https://" + url
    req  = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            try:
                rcv = response.read()
                ret = rcv.decode('utf-8')
            except UnicodeDecodeError:
                ret = rcv.decode('utf-8', 'replace')
            return ret
    except Exception as e:
        print(e)
        print("[%s] Error for URL: %s " % (datetime.datetime.now(), url))
        return None

def getJsonData(sigunguCode, areaCode, pageNo):
    server_key = "btp4HN6K1huIsR5HxQYsBaiMl239WaiwEas6zxFhFsnhuw6kag8Zu9BN6Ko6kMsQ5RRD19a%2BbNA%2FyCSbxoaWOw%3D%3D"
    url = "http://api.visitkorea.or.kr/openapi/service/rest/GreenTourService/areaBasedList"
    parameters = "?_type=json&serviceKey=" + server_key
    parameters += "&numOfRows=10"
    parameters += "&pageNo=" + pageNo
    parameters += "&arrange=C&MobileOS=ETC&MobileApp=AppTest"
    parameters += "&areaCode=" + areaCode
    parameters += "&sigunguCode="+ sigunguCode

    data = get_request_url(url + parameters)
    if data == None:
        return None
    else :
        return json.loads(data)


result = []
for i in range(1, 10):
    jsonData = getJsonData("1", "1", str(i))
    