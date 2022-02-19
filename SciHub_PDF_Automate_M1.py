import requests
from bs4 import BeautifulSoup
from time import sleep
import os
import wget
from tqdm import tqdm

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0', 'connection':'keep-alive'}    
print('******************************')
print('STARTING TO WRITE PDF FILES...')
file = open('dois.txt', 'r')
dois = file.readlines()
out = 'Pdfs'
for doi in tqdm(dois):
    try:
        base_url = 'https://sci-hub.se/'
        r = requests.get(base_url + doi.strip(), headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        cont = soup.find('embed').get('src').replace('#navpanes=0&view=FitH', '').replace('//', '/')
        if cont.startswith('/downloads'):
            pdf = 'https://sci-hub.se' + cont
        elif cont.startswith('/tree'):
            pdf = 'https://sci-hub.se' + cont
        elif cont.startswith('/uptodate'):
            pdf = 'https://sci-hub.se' + cont
        else:
            pdf = 'https:/' + cont
            
        wget.download(pdf, out=out)
        
        PDFs=open('PDF_FOUND.txt', 'a')
        PDFs.write(doi.strip() + '\t' + pdf.strip()+ '\n')
    except:
        NoPDF=open('PDF_NOT_FOUND.txt', 'a')
        NoPDF.write(doi.strip()+ '\n')
    sleep(3)

