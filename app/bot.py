from flask import Blueprint, request, jsonify

from domain.fizzbuzz import fizz_buzz

bot_blueprint = Blueprint('bot', __name__)


@bot_blueprint.route('/fizz-buzz', methods=['GET'])
def show():
    number = int(request.args.get('number'))
    result = fizz_buzz(number)
    return jsonify(result)

