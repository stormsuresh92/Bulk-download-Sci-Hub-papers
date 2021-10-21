import requests
from bs4 import BeautifulSoup
import time
import datetime



header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Connection':'keep-alive'
}

#url = 'https://sci-hub.se/10.1016/j.jtho.2016.12.014'
print('starting extraction process...')
start_time = datetime.datetime.now()
file = open('dois.txt', 'r')
dois = file.readlines()
for doi in dois:
    try:
        base_url = 'https://sci-hub.se/'   
        r = requests.get(base_url+doi.strip(), headers=header)
        soup = BeautifulSoup(r.content, 'html.parser')
        cont = soup.find(id='pdf').get('src').replace('#navpanes=0&view=FitH', '')
        if not cont.startswith('https:'):
            cont = 'https:'+str(cont)
        else:
            cont = cont
        output_file = open('URLs_output.tsv', 'a')
        output_file.write(doi.strip() + '\t' + str(cont) + '\n')  
        output_file.close()
    except:
        output_file = open('URLs_output.tsv', 'a')
        output_file.write(doi.strip() + '\t' + 'DOI Error' + '\n')
        end_time = datetime.datetime.now()   
        output_file.close()
    time.sleep(10)


print('File downloaded')
print('Time taken to task complete:', end_time-start_time)
