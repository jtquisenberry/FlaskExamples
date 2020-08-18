import pandas as pd
import pickle

class Document():
    def __init__(self):
        docs = {'docid':['a', 'b', 'c', 'd', 'e'], 'text':['aaa\nqqq', 'bbb', 'ccc', 'ddd', 'eee']}
        self.df = pd.DataFrame(docs)

        self.document_chunks = list()

        a = 1

    def get_chunks(self, doc_number):
        row = self.df.loc[0]
        docid, text = row
        lines = text.split('\n')

        self.document_chunks = list()

        line_number = 0
        for line in lines:
            doc = Document(docid, line_number, line)
            self.document_chunks.append(doc)


        b = 1

class DocumentSegment():
    def __init__(self, docid, line_number, text):
        self.docid = docid
        self.line_number = line_number
        self.text = text
