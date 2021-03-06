from setup_db import db
from marshmallow import Schema, fields


class Director(db.Model):
    __table_name__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
