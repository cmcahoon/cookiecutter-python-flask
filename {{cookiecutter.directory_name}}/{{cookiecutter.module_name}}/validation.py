from marshmallow import post_load
from .marshmallow import ma
from .model import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

    @post_load
    def make_model(self, data, **kwargs):
        return User(**data)
