from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='./playbook_withPAN.csv')
doc = loader.load()
print(doc[0].page_content) #First row of the file 