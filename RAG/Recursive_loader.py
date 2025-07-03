import requests
from bs4 import BeautifulSoup
from langchain_community.document_loaders import WebBaseLoader

url = 'http://docs.ansible.com/ansible/latest/collections/azure/azcollection/index.html#plugins-in-azure-azcollection'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

urls = []
for link in soup.find_all('a'):
    #print(link.get('href'))
    child = link.get('href')
    if child.startswith('azure'):
        site = f'https://docs.ansible.com/ansible/latest/collections/azure/azcollection/{child}'
        urls.append(site)
#print(urls)


loader = WebBaseLoader(urls[:10])
docs = loader.lazy_load()
for doc in docs:
    print(doc.metadata)