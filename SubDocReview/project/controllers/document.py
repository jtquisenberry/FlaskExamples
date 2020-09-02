
from project import app
from project import db
from flask import Flask, render_template, request, redirect, current_app, g
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from models.view_model import ViewModel
import json

breakpoint001 = 0

def cows():
    print('coweee')

breakpoint001 = 1

from models.grocery import Grocery
from models.document import Document
from models.document_segment_for_db import DocumentSegmentForDb




@app.route('/grocery', methods=['GET', 'POST'])
def index_grocery():
    if request.method == 'POST':
        name = request.form['name']
        new_stuff = Grocery(name=name)

        try:
            db.session.add(new_stuff)
            db.session.commit()
            return redirect('/')
        except:
            return "There was a problem adding new stuff."

    else:
        groceries = Grocery.query.order_by(Grocery.created_at).all()
        return render_template('index.html', groceries=groceries)


@app.route('/', methods=['GET', 'POST'])
def index():
    # if request.method == 'POST':
    if 1 % 2 == 0:  # Consider implementing POST later.
        name = request.form['name']
        new_stuff = Grocery(name=name)

        try:
            db.session.add(new_stuff)
            db.session.commit()
            return redirect('/')
        except:
            return "There was a problem adding new stuff."

    else:
        doc = app.config['doc']
        view_modelxxx = ViewModel(document=doc, test=42, row_number=0)
        return render_template('index5.html', view_model=view_modelxxx)


@app.route('/next/<int:row_num>', methods=['GET', 'POST'])
def index_next(row_num):
    row_num += 1
    view_model = index2(row_num=row_num, caller='index_next')
    return render_template('index5.html', view_model=view_model)


@app.route('/previous/<int:row_num>', methods=['GET', 'POST'])
def index_previous(row_num):
    row_num -= 1
    view_model = index2(row_num=row_num, caller='index_previous')
    return render_template('index5.html', view_model=view_model)


@app.route('/<int:row_num>', methods=['GET', 'POST'])
def index2(row_num=0, caller=''):
    if request.method == 'POST':

        print(request.json)
        segment_properties = dict()
        document_id = ''

        if request.is_json and isinstance(request.json, dict):
            if 'checkbox_ids' in request.json:
                for checkbox_id in request.json['checkbox_ids']:
                    pii_class, document_id, line_number = checkbox_id.split('^')
                    if document_id not in segment_properties:
                        segment_properties[document_id] = {line_number: list()}
                        segment_properties[document_id][line_number].append(pii_class)
                        b = 1
                    else:
                        if line_number not in segment_properties[document_id]:
                            segment_properties[document_id][line_number] = list()
                            segment_properties[document_id][line_number].append(pii_class)
                        else:
                            segment_properties[document_id][line_number].append(pii_class)

        a = 1

        pii_priority_order = {'BIRTH': 6, 'EMPAHI': 3, 'FINAN': 5, 'HEALI': 2, 'HEALINS': 0, 'MEDHIST': 1, 'WRE': 4 }

        for line_number, pii_classes in segment_properties[document_id].items():
            pii_classes.sort(key=lambda x: pii_priority_order[x])
            main_pii_class = pii_classes[0]
            all_pii_classes=';'.join(pii_classes)
            is_birth = ''
            is_empahi = ''
            is_heali = ''
            is_healins = ''
            is_medhist = ''
            is_wre = ''
            is_finan = ''
            for pii_class in pii_classes:
                is_birth = 'BIRTH' if pii_class == 'BIRTH' else is_birth
                is_empahi = 'EMPAHI' if pii_class == 'EMPAHI' else is_empahi
                is_heali = 'HEALI' if pii_class == 'HEALI' else is_heali
                is_healins = 'HEALINS' if pii_class == 'HEALINS' else is_healins
                is_medhist = 'MEDHIST' if pii_class == 'MEDHIST' else is_medhist
                is_wre = 'WRE' if pii_class == 'WRE' else is_wre
                is_finan = 'FINAN' if pii_class == 'FINAN' else is_finan

            new_record = DocumentSegmentForDb(document_id=document_id,
                                              line_number=line_number,
                                              main_pii_class=main_pii_class,
                                              is_birth=is_birth,
                                              is_empahi=is_empahi,
                                              is_heali=is_heali,
                                              is_healins=is_healins,
                                              is_medhist=is_medhist,
                                              is_wre=is_wre,
                                              is_finan=is_finan,
                                              all_pii_classes=all_pii_classes)

            dummy_breakpoint = 0
            try:
                db.session.add(new_record)
                db.session.commit()
            except:
                return "There was a problem adding new records."

        return 'Successfully read data in Python.'

    else:  # GET
        dc = app.config['dc']
        doc = Document(dc)
        if row_num >= len(dc.df):
            row_num = 0
        elif row_num < 0:
            row_num = len(dc.df) - 1

        doc.get_document_from_row(row_index=(row_num))
        view_model = ViewModel(document=doc, test=42, row_number=row_num)

        if not caller:
            return render_template('index5.html', view_model=view_model)
        else:
            return view_model

        # view_modelxxx.row_number = id + 1
        # Add error handling for id + 1 == len(dc.df)





@app.route('/delete/<int:id>')
def delete(id):
    grocery = Grocery.query.get_or_404(id)

    try:
        db.session.delete(grocery)
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem deleting data."


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    grocery = Grocery.query.get_or_404(id)

    if request.method == 'POST':
        grocery.name = request.form['name']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was a problem updating data."

    else:
        title = "Update Data"
        return render_template('update.html', title=title, grocery=grocery)


