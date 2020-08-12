from marshmallow import Schema, fields


class RequestSchema(Schema):
    number = fields.Integer()

