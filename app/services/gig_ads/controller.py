from flask import request, jsonify, g
from app.services.auth.services import token_required
from app.services.gig_ads.services import (
    create_gig_ad, get_all_gig_ads, get_gig_ad,
    get_gig_ads_by_performer, update_gig_ad, delete_gig_ad
)
from app.models.schemas.gig_ads_schema import gig_ad_schema, gig_ads_schema


# Create a new gig ad
@token_required
def create_gig():
    performer_id = g.user["sub"]
    data = request.get_json()

    try:
        new_ad = create_gig_ad(performer_id, data)
        return jsonify({
            "message": "Gig Ad created successfully",
            "gig_ad": gig_ad_schema.dump(new_ad)
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Get all gig ads
def get_all_gigs():
    ads = get_all_gig_ads()
    return jsonify(gig_ads_schema.dump(ads)), 200


# Get a specific gig ad by ID
def get_gig(ad_id):
    ad = get_gig_ad(ad_id)
    if ad:
        return jsonify(gig_ad_schema.dump(ad)), 200
    return jsonify({"error": "Gig Ad not found"}), 404


# Get all gigs for the current performer
@token_required
def get_my_gigs():
    performer_id = g.user["sub"]
    ads = get_gig_ads_by_performer(performer_id)
    return jsonify(gig_ads_schema.dump(ads)), 200


# Update a gig ad
@token_required
def update_gig(ad_id):
    data = request.get_json()
    ad = update_gig_ad(ad_id, data)

    if ad:
        return jsonify({
            "message": "Gig Ad updated successfully",
            "gig_ad": gig_ad_schema.dump(ad)
        }), 200
    return jsonify({"error": "Gig Ad not found"}), 404


# Delete a gig ad
@token_required
def delete_gig(ad_id):
    success = delete_gig_ad(ad_id)
    if success:
        return jsonify({"message": "Gig Ad deleted successfully"}), 200
    return jsonify({"error": "Gig Ad not found"}), 404