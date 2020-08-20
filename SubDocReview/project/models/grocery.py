from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from project import db
from flask import Flask, current_app, g

xxxxx = 4

class Grocery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    def __repr__(self):
        return '<Grocery %r>' % self.name