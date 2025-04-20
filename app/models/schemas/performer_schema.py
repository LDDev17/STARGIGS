from marshmallow import fields
from app import ma



class PerformerSchema(ma.Schema):
    id = fields.Integer(required=False) 
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    username = fields.String(required=True)
    email = fields.Email(required=True)
    phone = fields.Integer(required=True)
    city = fields.String(required=True)
    password = fields.String(required=True)


    class Meta: 
        fields = ("id", "first_name", "last_name","username", "email", "phone", "city", "password")


performer_schema = PerformerSchema()
performers_schema = PerformerSchema(many=True, exclude=["password"])
