import requests
from bs4 import BeautifulSoup

head = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'referer':'https://sci-hub.se/',
    'Connection':'keep-alive',
    'keep-alive':'timeout=60'
    }

proxy = {
    'http':'134.209.42.113:8899',
    'http':'170.155.5.235:8080'
    }

url = 'https://sci-hub.se/10.1016/j.jtho.2016.12.014'

r = requests.get(url, headers=head, proxies=proxy)
soup = BeautifulSoup(r.text, 'html.parser')
cont = soup.find('embed')
print(cont)
