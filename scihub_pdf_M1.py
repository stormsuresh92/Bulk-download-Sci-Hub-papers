import requests
from bs4 import BeautifulSoup
import wget
from tqdm import tqdm
from time import sleep


#url = 'https://sci-hub.se/10.1016/j.jtho.2016.12.014'
print('\n')
print('Writing pdf files....')

doilist = open('dois.txt', 'r')
dois = doilist.readlines()
output_folder = 'Downloaded pdfs'

for doi in tqdm(dois):
	try:
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

		wget.download(pdf, out=output_folder)

		pdfs = open('PDFs_Found.txt', 'a')
		pdfs.write(doi.strip() + '\t' + pdf + '\n')

	except:

		Nopdfs = open('PDFs_Not_Found.txt', 'a')
		Nopdfs.write(doi.strip() + '\n')

	sleep(3)

