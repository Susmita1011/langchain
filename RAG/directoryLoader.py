# Loads the folder / directory with multiple files in it to Langchain
# **/* .txt -> all txt from the subfolder , *.pdf -> root load all pdf, data/*.csv -> all scv from data/ folder, **/* all files any type all folder'
from langchain_community.document_loaders import DirectoryLoader,TextLoader

loader = DirectoryLoader(
    path='./text_folder',
    glob='*.txt',
    loader_cls=TextLoader   
    )
docs = loader.lazy_load() # for large documents and streaming using less memory . It outputs a generator of document
for document in docs:
    print(document)
