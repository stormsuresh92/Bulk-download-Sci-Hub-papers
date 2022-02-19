import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from time import sleep
import os



print('\n')
print('Writing pdf files....')

current_dir = os.getcwd()
output_folder = current_dir + '/Downloaded PDFs'
if not os.path.exists(output_folder):
	os.mkdir(output_folder)

doilist = open('dois.txt', 'r')
dois = doilist.readlines()

for doi in tqdm(dois):
	try:
		pdf_name = doi.strip()
		base_url = 'https://sci-hub.se/'
		response = requests.get(base_url + doi.strip())
		soup = BeautifulSoup(response.content, 'html.parser')
		content = soup.find('embed').get('src').replace('#navpanes=0&view=FitH', '').replace('//', '/')

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
		pdfs.write(doi.strip() + '\t' + pdf + '\n')

	except:

		Nopdfs = open('PDFs_Not_Found.txt', 'a')
		Nopdfs.write(doi.strip() + '\n')

	sleep(1)

