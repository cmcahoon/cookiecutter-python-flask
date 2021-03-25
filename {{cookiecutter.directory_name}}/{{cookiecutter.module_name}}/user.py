from flask import Blueprint, abort, request
from .db import db
from .model import User
from .validation import UserSchema


bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        abort(404)

    return UserSchema().dump(user)


@bp.route('', methods=['POST'])
def create_user():
    # Create an instance of the Marshmallow schema for input validation and
    # dumping the model to a dict.
    schema = UserSchema()

    # Validate the input
    body = request.json
    model = schema.load(body)

    # Add the new user to the database
    db.session.add(model)
    db.session.commit()

    # Return the commited module
    return schema.dump(model)
