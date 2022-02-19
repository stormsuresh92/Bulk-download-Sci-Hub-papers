import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from time import sleep
import os


headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
	'Connection':'keep-alive'
}

print('\n')
print('Writing pdf files....')

current_dir = os.getcwd()
output_folder = current_dir + '/Downloaded PDFs'
if not os.path.exists(output_folder):
	os.mkdir(output_folder)

PMIDlist = open('Input_IDs.txt', 'r')
pmids = PMIDlist.readlines()
for ids in tqdm(pmids):
	try:
		payload = {
		'sci-hub-plugin-check':'',
		'request':str(ids.strip())
		}

		pdf_name = ids.strip()
		base_url = 'https://sci-hub.se/'
		response = requests.post(base_url, headers=headers, data=payload, timeout=60)
		soup = BeautifulSoup(response.content, 'html.parser')
		content = soup.find(id='pdf').get('src').replace('#navpanes=0&view=FitH', '').replace('//', '/')

		if content.startswith('/downloads'):
			pdf = 'https://sci-hub.se' + content

		elif content.startswith('/tree'):
			pdf = 'https://sci-hub.se' + content

		elif content.startswith('/uptodate'):
			pdf = 'https://sci-hub.se' + content

		else:
			pdf = 'https:/' + content

		r = requests.get(pdf, stream=True)
		with open(output_folder + '/' + pdf_name.replace('/', '-') + '.pdf', 'wb') as file:
			file.write(r.content)

		pdfs = open('PDFs_Found.txt', 'a')
		pdfs.write(ids.strip() + '\t' + pdf + '\n')

	except:

		Nopdfs = open('PDFs_Not_Found.txt', 'a')
		Nopdfs.write(ids.strip() + '\n')

	sleep(1)
