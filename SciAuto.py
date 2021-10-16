import requests
import time
import os
import datetime


header = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'cookie': '__ddg1=vIZdy9vxnQG4nUio57zQ; session=0110d1d0ad673d3b1e0398e2e5ead499; __ddgid=ratXmk3e9CJ0O1M9; _ym_uid=1627210666935448269; _ym_d=1627210666; __ddg2=GCD2Zk9ymK4bFSZS; refresh=1634294503.4645; _ym_isad=2',
    'referer': 'https://sci-hub.se/',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Connection':'keep-alive'
}

cur_dir = os.getcwd()
pdf = cur_dir + '/pdfs'
if not os.path.exists(pdf):
    os.mkdir(pdf)

start_time = datetime.datetime.now()
file = open('pdf.txt', 'r')
pdfu = file.readlines()
for port in pdfu:
    try:
        title = port.split('/')[-1].replace('.pdf', '').strip()
        pdf_url = requests.get(port, stream=True)
        print('Downloaded', '=>', title)
        with open(pdf + '/' + title + '.pdf', 'wb') as f:
            for chunk in pdf_url.iter_content(2000):
                f.write(chunk)
        time.sleep(2)
        end_time = datetime.datetime.now()
        f.close()
    except:
        pass


print(':::::::::::::::::::::::')    
print('Time taken to task complete:', end_time-start_time)
