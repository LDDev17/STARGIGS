from flask import Blueprint
#from payments.controllers import process_payment, get_payment_status, get_all_payments

payments_blueprint = Blueprint('payments_bp', __name__)

payments_blueprint.route('/', methods=['POST'])#(process_payment) 
payments_blueprint.route('/<int:id>', methods=['GET'])#(get_payment_status) 
payments_blueprint.route('/', methods=['GET'])#(get_all_payments)  