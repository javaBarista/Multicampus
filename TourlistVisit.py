import urllib.request
import datetime
import time
import json
import pandas
import matplotlib.pyplot as plt
import matplotlib

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

def getNatVisitor(yyyymm, nat_cd, ed_cd):
    service_key = "btp4HN6K1huIsR5HxQYsBaiMl239WaiwEas6zxFhFsnhuw6kag8Zu9BN6Ko6kMsQ5RRD19a%2BbNA%2FyCSbxoaWOw%3D%3D"
    url = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
    parameters = '?_type=json&serviceKey=' + service_key
    parameters += '&YM=' + yyyymm
    parameters += '&NAT_CD=' + nat_cd
    parameters += '&ED_CD=' + ed_cd

    retData = get_request_url(url + parameters)
 
    if retData == None:
        return None
    else: return json.loads(retData)

result = []
for year in range(2015, 2016):
    for month in range(1, 13):
        yyyymm = '{0}{1:0>2}'.format(str(year), str(month))
        json_Data = getNatVisitor(yyyymm, "275", "E")
        #print(json.dumps(json_Data, indent=4, sort_keys=True, ensure_ascii="False"))

        if(json_Data['response']['header']['resultMsg'] == 'OK'):
            krName = json_Data['response']['body']['items']['item']['natKorNm']
            krName = krName.replace(' ','')
            iTotalVisit = json_Data['response']['body']['items']['item']['num']
            print("%s_%s : %s" %(krName,yyyymm, iTotalVisit))
            result.append([yyyymm] + [krName] + ['275'] + [iTotalVisit])


pandas.DataFrame(result).to_csv("%s_해외방문자_%s" % ('275', '2015') + '.csv', encoding = 'cp949', header = "None", index = 'False')

cnVisit = []
visitYM = []
index = []
i = 0
for item in result:
    index.append(i)
    cnVisit.append(item[3])
    visitYM.append(item[0])
    i += 1

plt.xticks(index, visitYM)
plt.plot(index, cnVisit)
plt.grid(True)
plt.show()