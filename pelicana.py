import bs4
import urllib.request as ur
import pandas
import Get_URL
from itertools import count

result = []
for z in count():
    url = 'https://pelicana.co.kr/store/stroe_search.html?page=%s' % str(z+1)
    #html = ur.urlopen(url)
    html = Get_URL.get_request_url(url, "utf-8")
    soupData = bs4.BeautifulSoup(html, 'html.parser')
    table = soupData.find('table', {'class':'table mt20'})
    tbody = table.find('tbody')
    #store = list(tbody.find_all('tr')[0].strings)

    beEnd = True
    for i in tbody.find_all('tr'):
        beEnd = False
        store = list(i.strings)
        store_name = store[1]
        store_address = store[3]
        store_phone = store[5].strip()
        store_sido_gu = store_address.split()[:2]

        result.append([store_name] + [store_address] + [store_phone] + [store_sido_gu])
    if beEnd : break
    print("페리카나 [%s] 페이지 크롤링 중" % (str(z + 1)))

pelicana = pandas.DataFrame(result, columns=['store', 'address', 'phone', 'sido-gu'])
pelicana.to_csv('pelicana2.csv', encoding="cp949", index=True)