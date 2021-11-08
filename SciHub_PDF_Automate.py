import requests
from bs4 import BeautifulSoup
import time
import os
from tqdm import tqdm



header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Connection':'keep-alive',
    'Keep-Alive': 'timeout=60'
}

cur_dir = os.getcwd()
pdf = cur_dir + '/Downloaded PDFs'
if not os.path.exists(pdf):
    os.mkdir(pdf)

print('STARTING EXTRACTION PROCESS...')
file = open('Input_PMIDs.txt', 'r')
pmids= file.readlines()
for pmid in tqdm(pmids):
    time.sleep(0.02)
    try:
        payload={
            'sci-hub-plugin-check':'',
            'request':str(pmid.strip())
        }
        base_url = 'https://sci-hub.se/'
        r = requests.post(base_url, headers=header, data=payload)
        soup = BeautifulSoup(r.content, 'html.parser')
        cont = soup.find(id='pdf').get('src').replace('#navpanes=0&view=FitH', '')
        if not cont.startswith('https:'):
            pdfurl = 'https:'+str(cont)
        else:
            pdfurl = cont
        
        res = requests.get(pdfurl, stream=True)
        #print('Writing to pdf:', pmid.strip())
        with open(pdf + '/' + pmid.strip() + '.pdf', 'wb') as f:
            for chunk in res.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
             
    except:
        #print('PDF Url Not Found:', pmid.strip())
        NoPDF=open('NoPDF.txt', 'a')
        NoPDF.write(pmid.strip())
    time.sleep(20)