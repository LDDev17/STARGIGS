from marshmallow import Schema, fields

class GigAdSchema(Schema):
    id = fields.Integer(dump_only=True)
    performer_id = fields.Integer(required=True)
    title = fields.String(required=True)
    description = fields.String()
    gig_type = fields.String(required=True)
    location = fields.String()
    hourly_rate = fields.Float(required=True)
    media_url = fields.String()
    thumbnail_url = fields.String()
    availability = fields.Dict()  # Expects {"available": [...], "blocked": [...]}
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    class Meta:
        fields = (
            "id", "performer_id", "title", "description", "gig_type", "location",
            "hourly_rate", "media_url", "thumbnail_url", "availability",
            "created_at", "updated_at"
        )

gig_ad_schema = GigAdSchema()
gig_ads_schema = GigAdSchema(many=True)