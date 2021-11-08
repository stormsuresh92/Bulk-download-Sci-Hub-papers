import requests
from bs4 import BeautifulSoup
import time
import datetime



header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Connection':'keep-alive'
}

print('STARTING EXTRACTION PROCESS...')
start_time = datetime.datetime.now()
file = open('Input.txt', 'r')
dois = file.readlines()
for doi in dois:
    try:
        payload={
            'sci-hub-plugin-check':'',
            'request':str(doi)
        }
        base_url = 'https://sci-hub.se/'
        r = requests.post(base_url, headers=header, data=payload)
        soup = BeautifulSoup(r.content, 'html.parser')
        cont = soup.find(id='pdf').get('src').replace('#navpanes=0&view=FitH', '')
        Pdfname = soup.find(id='pdf').get('src').replace('#navpanes=0&view=FitH', '').split('/')[-1].replace('.pdf', '')
        if not cont.startswith('https:'):
            cont = 'https:'+str(cont)
        else:
            cont = cont
        print('PDF Available', '=>', doi.strip(), '##', datetime.datetime.now())
        output_file = open('PDFURLs.tsv', 'a')
        output_file.write(doi.strip() + '\t' + str(cont) + '\t' + Pdfname + '\n')
        output_file.close()
    except:
        print('NoPDF', '=>', doi.strip(), '##', datetime.datetime.now())
        output_file = open('No_Pdf.txt', 'a')
        output_file.write(doi.strip() + '\n')
        end_time = datetime.datetime.now()   
        output_file.close()
    time.sleep(15)
    

print('****************')
print('Time taken to task completed:', end_time-start_time)
print('****************')
