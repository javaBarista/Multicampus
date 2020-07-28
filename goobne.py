from selenium import webdriver
from itertools import count
import time
from bs4 import BeautifulSoup
import pandas as pd

def GoobneAddress():
    url = "https://www.goobne.co.kr/store/search_store.jsp"
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(url)
    result = []

    for z in count():
        driver.execute_script('store.getList(%s)' % str(z + 1))
        time.sleep(2)
        rcv_data = driver.page_source
        soupData = BeautifulSoup(rcv_data, 'html.parser')

        for storelist in soupData.findAll('tbody', {'id':"store_list"}):
            for store in storelist:
                tr_tag = list(store.strings)
                if tr_tag[0] == '등록된 데이터가 없습니다.': 
                    return result

                store_name = tr_tag[1]
                store_phone = tr_tag[3]
                store_address = tr_tag[6]
                store_sido_gu = store_address.split()[:2]
                result.append([store_name] + [store_sido_gu] + [store_address] + [store_phone])

result = GoobneAddress()
goobne = pd.DataFrame(result, columns=['store', 'sido-gu', 'address', 'phone'])
goobne.to_csv('goobne.csv', encoding="cp949", index=True)
print("저장완료")