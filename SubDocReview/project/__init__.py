from flask import Flask, render_template, request, redirect, current_app, g, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



__version__ = '1.00'
from flask import Flask
app = Flask(__name__)
app.debug = True

#Sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///document_segments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


with app.app_context():

    db = SQLAlchemy(app)

    # Pickled documents data store.
    from .models.document import Document, DocumentContainer, DocumentSegment
    pickle_path = r'C:\corpora\insurance_company\insurance_documents.pkl'
    dc = DocumentContainer()
    dc.get_documents_from_pickle(pickle_path)
    doc = Document(document_container=dc)
    doc.get_document_from_row(0)
    app.config['dc'] = dc
    app.config['doc'] = doc




    # from project.controllers import *  # This enables importing all the modules in the controllers package.
    from project.controllers import document
    document.cows()





q = 1
