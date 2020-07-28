import bs4

html_str = "<html><div>hello</div></html>"
result = bs4.BeautifulSoup(html_str, 'html.parser')

print(result.find('div').text)