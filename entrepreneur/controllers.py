from flask import Blueprint, jsonify
from flask import request
from entrepreneur.base import entre_main


entrepreneur_blueprint = Blueprint('entrepreneur', __name__)


@entrepreneur_blueprint.route('/get_news')
def entrepreneur():
    """
    This is the summary defined in yaml file
    First line is the summary
    All following lines until the hyphens is added to description
    the format of the first lines until 3 hyphens will be not yaml compliant
    but everything below the 3 hyphens should be.
    ---
    tags:
     - Entrepreneur
    description: gets one page of entrep channel news
    parameters:
     - name: category
       in: query
       type: string
       required: true
     - name: page
       in: query
       type: integer
       required: true
    """
    category = request.args.get('category')
    page = request.args.get('page')
    return jsonify(entre_main(category=category, page=page))
