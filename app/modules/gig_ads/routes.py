from flask import Blueprint
from app.modules.gig_ads.controller import (
    create_gig, get_all_gigs, get_gig, get_my_gigs,
    update_gig, delete_gig
)

gig_ads_blueprint = Blueprint("gig_ads_bp", __name__, url_prefix="/gigs")

# Public routes
gig_ads_blueprint.route("/", methods=["GET"])(get_all_gigs)
gig_ads_blueprint.route("/<int:ad_id>", methods=["GET"])(get_gig)

# Performer-specific routes (protected)
gig_ads_blueprint.route("/me", methods=["GET"])(get_my_gigs)
gig_ads_blueprint.route("/", methods=["POST"])(create_gig)
gig_ads_blueprint.route("/<int:ad_id>", methods=["PUT"])(update_gig)
gig_ads_blueprint.route("/<int:ad_id>", methods=["DELETE"])(delete_gig)