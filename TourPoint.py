import urllib.request
import datetime
import time
import math
import json
import pandas 

result = []
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

def getItemFormPointData(yyymm, sido, gnugu, nPageNum, nItems):
    access_key="btp4HN6K1huIsR5HxQYsBaiMl239WaiwEas6zxFhFsnhuw6kag8Zu9BN6Ko6kMsQ5RRD19a%2BbNA%2FyCSbxoaWOw%3D%3D"
    url = "http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList"
    parameter = '?_type=json&serviceKey=' + access_key
    parameter += '&YM=' + yyymm
    parameter += '&SIDO=' + urllib.parse.quote(sido)
    parameter += '&GUNGU=' + urllib.parse.quote('')
    parameter += '&RES_NM=&pageNo=' + str(nPageNum)
    parameter += '&numOfRows=' + str(nItems)
    
    url += parameter
    retData = get_request_url(url)
    if retData == None:
        return None
    else: 
        return json.loads(retData)

for year in range(2011, 2020):
    for month in range(1, 13):
        yyyymm = "{0}{1:0>2}".format(str(year), str(month))
        nPageNum = 1
        while True:
            jsonData = getItemFormPointData(yyyymm, '서울특별시', '', 1, 100)
            print("%s tourplace of the seoul crolling....." % yyyymm)
            if jsonData['response']['header']['resultMsg'] == 'OK':
                nTotal = jsonData['response']['body']['totalCount']
                if nTotal == 0: break

                for item in jsonData['response']['body']['items']['item']:
                    sido = '' if 'sido' not in item.keys() else item['sido']
                    gungu = '' if 'gungu' not in item.keys() else item['gungu']
                    resNm = '' if 'resNm' not in item.keys() else item['resNm']
                    rnum = 0 if 'rnum' not in item.keys() else item['rnum']
                    addrCd = 0 if 'addrCd' not in item.keys() else item['addrCd']
                    csForCnt = 0 if 'csForCnt' not in item.keys() else item['csForCnt']
                    csNatCnt = 0 if 'csNatCnt' not in item.keys() else item['csNatCnt']

                    if 'csForCnt' in item.keys(): 
                        result.append([yyyymm] + [sido] + [gungu] + [resNm])
                nPage = math.ceil(nTotal/100)
                if(nPageNum == nPage): break
                nPageNum += 1
            else: break

pandas = pandas.DataFrame(result)
print(pandas)
#pandas.to_csv('tourpoint.csv', encoding='cp949', header=None, index="False")