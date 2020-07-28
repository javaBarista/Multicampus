import urllib.request 
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs = bs4.BeautifulSoup(html, 'html.parser')
ul = bs.find_all("a", {'class':'nav'})
#li = ul.find_all('a', {'class':'nav'})
for i in ul:
    print(i.text)