from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager

from security import authenticate, identity
from resources.user import UserRegister, User, UserLogin, TokenRefresh, UserLogout
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db
from blacklist import BLACKLIST


# flask_restful преобразует в json самостоятельно
# flask_jwt - для авторизации

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # отключаем дополнительную нагрузку
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.secret_key = 'python'
api = Api(app)

@app.before_first_request
def create_tables():
	db.create_all()  # заменяет модуль create_tables


jwt = JWTManager(app)  # / not creating /auth


@jwt.user_claims_loader
def add_claims_to_jwt(identity):
	if identity == 1:
		return {'is_admin': True}
	return {'is_admin': False}

@jwt.expired_token_loader
def expired_token_callback():
	return jsonify({
		'description': 'The token has expired',
		'error': 'token_expired'
	}), 401

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
	return decrypted_token['jti'] in BLACKLIST


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')
api.add_resource(TokenRefresh, '/refresh')
api.add_resource(UserLogout, '/logout')

if __name__ == '__main__':
	db.init_app(app)
	app.run(port=5000, debug=True)
