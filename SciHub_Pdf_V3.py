from requests_html import HTMLSession
import time
import datetime

s = HTMLSession()

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

#url = 'https://sci-hub.se/10.1016/j.jtho.2016.12.014'
print('starting extraction process...')
start_time = datetime.datetime.now()
file = open('dois.txt', 'r')
dois = file.readlines()
for doi in dois:
    try:
        base_url = 'https://sci-hub.se/'   
        r = s.get(base_url+doi.strip(), headers=header)
        cont = r.html.find('#pdf', first=True).attrs['src'].replace('#navpanes=0&view=FitH', '')
        print(cont)
        time.sleep(1)
        output_file = open('PDF_Availabl.tsv', 'a')
        output_file.write(doi.strip() + '\t' + str(cont) + '\n')  
        output_file.close()
    
    except:
        output_file = open('No_PDF.tsv', 'a')
        output_file.write(doi.strip() + '\t' + 'No PDF' + '\n')
        end_time = datetime.datetime.now()   
        output_file.close()

print('File downloaded')
print('Time taken to task complete:', end_time-start_time)