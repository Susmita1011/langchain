# pip install pypdf
from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader(file_path='./SVM.pdf') # only works for the simple documents but not great with scanned pdf/tabular data()
docs = loader.load()
print(len(docs))
print(docs[1].page_content)
print(docs[0].metadata)

# Tabular data pdf -> PDFPlumberLoader
#Scanned PDF -> UnstructuredPDFLoader
#Need layout & Image data -> PyMuPDFLoader
#Want best structure loader : UnstructuredPDFLoader

