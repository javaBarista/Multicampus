from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from itertools import count

url = 'http://tour.interpark.com/'
driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)
driver.find_element_by_id("SearchGNBText").send_keys('파리')
driver.find_element_by_class_name("search-btn").click()
try:
    WebDriverWait(driver, 3).until(EC.presence_of_all_element_located(By.CLASS_NAME, "moreBtn"))
except Exception as e:
    print("Error ", e)
#driver.implicitly_wait(2)
driver.find_element_by_css_selector('.moreBtnWrap>.moreBtn').click()
time.sleep(1)

result=[]
for z in count():
    driver.execute_script("searchModule.SetCategoryList([%s], '')" % (z + 1))
    time.sleep(2)
    boxItems = driver.find_elements_by_css_selector(".oTravelBox>.boxList>li")
    for item in boxItems:
        print("="*50)
        print("상품명: "+ item.find_element_by_css_selector('h5.proTit').text)
        print("가격 : "+ item.find_element_by_css_selector('.proPrice').text)
        print("정보 : "+ item.find_elements_by_css_selector('.info-row .proInfo')[1].text)