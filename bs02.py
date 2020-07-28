import bs4

html_str = '''
<html>
    <body>
        <ul class="great">
            <li>hello</li>
            <li>by</li>
            <li>welcome</li>
        </ul>
        <ul class="reply">
            <li>ok</li>
            <li>no</li>
            <li>sure</li>
        </ul>
    </body>
</html>
'''

bs = bs4.BeautifulSoup(html_str, 'html.parser')
for i in bs.find_all('li'):
    print(i.text)