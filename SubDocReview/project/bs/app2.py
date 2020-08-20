# Based on FlaskCRUD

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from models.document import DocumentContainer
from models.document import Document

app = Flask(__name__)

#Sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

def yyy():
    print('yyy')


from models.grocery import Grocery

# Pickled documents data store.
pickle_path = r'C:\corpora\allied_insurance\applied_insurance_documents.pkl'
dc = DocumentContainer()
dc.get_documents_from_pickle(pickle_path)
doc = Document(document_container=dc)
doc.get_document_from_row(0)
b = 1






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








@app.route('/grocery', methods=['GET', 'POST'])
def index():
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


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5555)
