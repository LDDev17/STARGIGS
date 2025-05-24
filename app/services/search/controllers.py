from flask import request, jsonify
from app.services.search.services import search_performers_services
from app.models.schemas.performer_schema import performers_schema

def search_performers_controller():
    filters = request.args.to_dict()
    results= search_performers_services(filters)
    
    if results:    
        return jsonify(performers_schema.dump(results)), 200
    
    return jsonify({"message": "no results found"}), 404