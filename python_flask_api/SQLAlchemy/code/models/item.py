from db import db


class ItemModel(db.Model): # Показываем SQLAlchemy что данный класс будет в бд
	__tablename__ = 'items'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	price = db.Column(db.Float(precision=2))

	store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
	store = db.relationship('StoreModel')

	def __init__(self, name, price, store_id):
		self.name = name
		self.price = price
		self.store_id = store_id

	def json(self):
		return {'name': self.name, 'price': self.price, 'store_name': self.store.name}

	@classmethod
	def find_by_name(cls, name):
		return cls.query.filter_by(name=name).first() # SELECT * FROM items WHERE name=name

	def save_to_db(self):
		db.session.add(self) 
		# Так как мы смотрим еще и на id то данный метод будет выполнять метод update
		db.session.commit()

	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()