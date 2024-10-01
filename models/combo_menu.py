from .base import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .combo_menu_detail import combo_menu_detail  # Import intermediate table

class ComboMenu(db.Model):
    __tablename__ = 'combo_menu'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    cafe_id = Column(Integer, ForeignKey('cafe.id'), nullable=False)
    item_type_id = Column(Integer, ForeignKey('item_type.id'), nullable=False)

    cafe = relationship('Cafe')
    item_type = relationship('ItemType')

    # Change the backref name to avoid conflicts
    products = relationship('Product', secondary=combo_menu_detail, backref='combo_menus')

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "cafe_id": self.cafe_id,
            "item_type_id": self.item_type_id,
            "products": [product.serialize() for product in self.products]
        }
