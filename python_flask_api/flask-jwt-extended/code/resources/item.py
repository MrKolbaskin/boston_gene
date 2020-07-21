from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_claims, jwt_optional, get_jwt_identity
from models.item import ItemModel

# reqparse - для парсинга request


class Item(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument(
		'price',
		type=float,
		required=True,
		help='This field cannot be left blank'
	)
	parser.add_argument(
		'store_id',
		type=int,
		required=True,
		help='Every item need a store id'
	)

	@jwt_required
	def get(self, name):
		item = ItemModel.find_by_name(name)
		if item:
			return item.json()
		return {'message': 'Item not found'}, 404

	def post(self, name):
		if ItemModel.find_by_name(name):
			return {'message': "This item with name '{}' already exists.".format(name)}, 400
		
		data = Item.parser.parse_args()

		item = ItemModel(name, **data)
		
		try:
			item.save_to_db()
		except:
			return {'message': 'An error occurred inserting the item.'}, 500

		return item.json(), 201

	@jwt_required
	def delete(self, name):
		claims = get_jwt_claims()
		if not claims['is_admin']:
			return {'message': 'Admin privilege required'}, 401

		item = ItemModel.find_by_name(name)
		
		if item:
			try:
				item.delete_from_db()
			except:
				return {"message": 'An error occurred deleting the item.'}, 500

		return {'message': 'Item deleted'}

	def put(self, name):
		data = Item.parser.parse_args() #других аргументов, даже если они будут их не будет видно

		item = ItemModel.find_by_name(name)

		if item is None:
			item = ItemModel(name, **data)
		else:
			item.price = data['price']

		try:
			item.save_to_db()
		except:
			return {"message": 'An error occurred adding the item.'}, 500
		
		return item.json()


class ItemList(Resource):
	@jwt_optional
	def get(self):
		user_id = get_jwt_identity()
		items = [item.json() for item in ItemModel.query.all()]
		if user_id:
			return {'items': items}
		return {
			'items': [item['name'] for item in items],
			'message': 'More data available if you log in'
		}
