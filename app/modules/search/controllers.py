from flask import request, jsonify
from app.modules.search.services import search_performers_services
from app.models.schemas.performer_schema import performers_schema

# Controller to handle performer search requests
def search_performers_controller():
    # Extract search filters from query parameters
    filters = request.args.to_dict()
    # Call the service to perform the search
    results = search_performers_services(filters)
    
    if results:    
        # Return serialized results if found
        return jsonify(performers_schema.dump(results)), 200
    
    # Return a message if no results are found
    return jsonify({"message": "no results found"}), 404