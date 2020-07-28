from itertools import count
from bs4 import BeautifulSoup
import pandas 
import time
import Get_URL

result = []
def makelist(num1):
    global result
    for num2 in count():
        try:
            url = "http://www.kyochon.com/shop/domestic.asp?sido1=%s&sido2=%s" % (str(num1 + 1), str(num2 + 1))
            html = Get_URL.get_request_url(url, "utf-8")
            soupData = BeautifulSoup(html, 'html.parser')
            table = soupData.find('ul', {'class':"list"})
            beEnd = True
            for i in table.find_all('strong'):
                beEnd = False
                store_name = i.text
                add = list(table.find('em').strings)
                store_sido_gu = add[0].strip()
                store_address = add[1].strip()
                store_phone = add[2].strip()
                result.append([store_name] + [store_sido_gu] + [store_address] + [store_phone])

            if beEnd : break
            print("교촌 [%s] & [%s] 페이지 크롤링 중" % (str(num1 + 1), str(num2 + 1)))
        except Exception as e:
            print("행정구역 완료")
            break


for num1 in range(17):
    makelist(num1)

kyochon = pandas.DataFrame(result, columns=['store', 'sido-gu', 'address', 'phone'])
print(kyochon)