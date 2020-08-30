import pandas as pd
import pickle
from flask import Flask, current_app, g, session

mmmm = 0

class DocumentContainer():
    def __init__(self):

        # A Dataframe containing all documents.
        self.df = None

    def get_documents_from_pickle(self, pickle_path=None):

        if not pickle_path:
            docs = {'docid':['a', 'b', 'c', 'd', 'e'], 'text':['aaa\nqqq', 'bbb', 'ccc', 'ddd', 'eee']}
            self.df = pd.DataFrame(docs)
        else:
            # Pickle
            # pickle_path = r'C:\corpora\allied_insurance\applied_insurance_documents.pkl'
            print('Loading Pickle {0}'.format(pickle_path))
            self.df = pd.read_pickle(pickle_path)
            print('Pickle loaded')

    def __repr__(self):
        out_string = 'Document Count = {0}'.format(self.df.shape)
        return out_string

    def __str__(self):
        out_string = 'Document Count = {0}'.format(self.df.shape)
        return out_string


class Document():
    def __init__(self, document_container):

        if document_container is None:
            raise ValueError('The document_container must be a non-empty Dataframe')

        self.df = document_container.df
        self.document_id = ''
        self.pii_classes = ''
        self.old_id = ''
        self.text = ''
        self.word_counts_str = ''
        self.character_counts_str = ''
        self.segments = list()

    def __repr__(self):
        out_string = self.document_id
        return out_string

    def __str__(self):
        out_string = self.document_id
        return out_string

    def get_document_from_row(self, row_index=0):
        row = self.df.loc[row_index]
        self.document_id, self.pii_classes, self.old_id, self.text, self.word_counts_str, self.character_counts_str = row
        self._get_chunks(line_delimiter=(chr(0x20001)))  # 𠀁

    def _get_chunks(self, line_delimiter=chr(0x20001)):
        # lines = text.split('\n')
        lines = self.text.split(line_delimiter)
        word_counts = self.word_counts_str.split(line_delimiter)
        word_counts = [int(x) for x in word_counts]
        character_counts = self.character_counts_str.split(line_delimiter)
        character_counts = [int(x) for x in character_counts]

        for line_number in range(0, len(lines)):
            ds = DocumentSegment(document_id=self.document_id, line_number=line_number, line=lines[line_number],
                                 word_count=word_counts[line_number], character_count=character_counts[line_number])
            self.segments.append(ds)
            line_number += 1

        a = 1


class DocumentSegment():
    def __init__(self, document_id, line_number, line, word_count, character_count):
        self.document_id = document_id
        self.line_number = line_number
        self.line = line
        self.word_count = word_count
        self.character_count = character_count

    def __repr__(self):
        out_string = self.line[0:20]
        return out_string

    def __str__(self):
        out_string = self.line[0:20]
        return out_string
