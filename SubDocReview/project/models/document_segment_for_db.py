from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from project import db
from flask import Flask, current_app, g

dummy_breakpoint = 0


'''
label_to_short = {
    'Birth Certificate': 'BIRTH',
    'Employee Account Information': 'EMPAHI',
    'Health Information': 'HEALI',
    'Health Insur App/Claims Info': 'HEALINS',
    'Medical History, Condition, Treatment, or Diagnosis': 'MEDHIST',
    'Work-Related Evaluations': 'WRE',
    'Passport Number': 'PSPRT',
    'Financial Account Number with Password or Routing Number': 'FINAN',
    'Financial Account Number without Password or Routing Number': 'FINAN'
}
'''




class DocumentSegmentForDb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    document_id = db.Column(db.String(80), nullable=False)
    line_number = db.Column(db.String(80), nullable=False)
    main_pii_class = db.Column(db.String(80), nullable=False)
    is_birth = db.Column(db.String(80), nullable=False, default='')
    is_empahi = db.Column(db.String(80), nullable=False, default='')
    is_heali = db.Column(db.String(80), nullable=False, default='')
    is_healins = db.Column(db.String(80), nullable=False, default='')
    is_medhist = db.Column(db.String(80), nullable=False, default='')
    is_wre = db.Column(db.String(80), nullable=False, default='')
    is_finan = db.Column(db.String(80), nullable=False, default='')
    all_pii_classes = db.Column(db.String(160), nullable=False, default='')
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    def __repr__(self):
        return '<DocumentSegmentForDb %r>' % self.document_id + self.line_number

    def __str__(self):
        return '<DocumentSegmentForDb %r>' % self.document_id + self.line_number