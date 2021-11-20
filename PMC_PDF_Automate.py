from requests_html import HTMLSession
import os
import time
from tqdm import tqdm
import logging
from requests.exceptions import ConnectionError

s = HTMLSession()


headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'connection':'keep-alive'
}

logging.basicConfig(filename='Logfile.log', level=logging.DEBUG, 
                    format='%(asctime)s-%(message)s', datefmt='%d-%b-%y %H-%M-%S')

cur_dir = os.getcwd()
pdf = cur_dir + '/Downloaded PDFs'
if not os.path.exists(pdf):
    os.mkdir(pdf)

print('******************************')
print('STARTING TO WRITE PDF FILES...') 
input_file = open('Input_PMC_Urls.txt', 'r')
urls = input_file.readlines()
for url in tqdm(urls):
    urllist = url.strip()
    try:
        r = s.get(urllist, headers=headers)
        pdfs = r.html.find('#main-content > aside > section:nth-child(1) > ul > li.pdf-link.other_item')
        for item in pdfs:
            pmcpdf = 'https://www.ncbi.nlm.nih.gov' + item.find('a', first=True).attrs['href']
            pmcid = item.find('a', first=True).attrs['href'].split('/')[-3]
            res = s.get(pmcpdf, stream=True)
            with open(pdf + '/' + pmcid.strip() + '.pdf', 'wb') as f:
                for chunk in res.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        
    except ConnectionError as e:
        pass
        file = open('Connection_Error_Urls.txt', 'a')
        file.write(urllist + '\n')
    time.sleep(5)
    

