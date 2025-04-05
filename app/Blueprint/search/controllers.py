from flask import request, jsonify
from app.Blueprint.search.services import search_performers_services
from app.models.schemas.performerSchema import performers_schema

def search_performers_controller():
    filters = request.args.to_dict()
    results= search_performers_services(filters)

    return jsonify(performers_schema.dump(results)), 200