from marshmallow import Schema, fields

class BookingSchema(Schema):
    id = fields.Int()
    client_id = fields.Str()
    performer_id = fields.Str()
    event_date = fields.Date()
    location = fields.Str()
    price = fields.Float()
    status = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

booking_schema = BookingSchema()
bookings_schema = BookingSchema(many=True)