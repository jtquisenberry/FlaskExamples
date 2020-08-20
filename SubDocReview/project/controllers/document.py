
from project import app
from project import db
from flask import Flask, render_template, request, redirect, current_app, g
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

breakpoint001 = 0

def cows():
    print('coweee')

breakpoint001 = 1

from models.grocery import Grocery

'''
@app.route('/', methods=['GET', 'POST'])
def indexa():
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
        # return render_template('index.html', groceries=groceries)

        grocery1 = Grocery()
        grocery2 = Grocery()
        grocery1.id = 111
        grocery1.name = 'name111'
        grocery1.created_at = 'aaaa'
        grocery2.id = 111
        grocery2.name = 'name111'
        grocery2.created_at = 'aaaa'


        return render_template('index2.html', groceries=[grocery1, grocery2])
'''


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
        return render_template('index5.html', groceries=doc)





@app.route('/<int:id>', methods=['GET', 'POST'])
def index2(id):
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
        groceries = Grocery.query.order_by(Grocery.created_at).all()
        return render_template('index.html', groceries=groceries)

















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

