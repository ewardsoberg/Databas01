from db import Base
import sqlalchemy as sa


class Shop(Base):

    __tablename__ = 'shops'

    id = sa.Column(sa.Integer, primary_key=True)
    phone = sa.Column(sa.String(25), nullable=False)
    email = sa.Column(sa.String(45), nullable=False)
    address_line_one = sa.Column(sa.String(100), nullable=False)
    address_line_two = sa.Column(sa.String(100), nullable=False)
    city = sa.Column(sa.String(192), nullable=False)
    country = sa.Column(sa.String(60), nullable=False)

    def __repr__(self):
        return f'Shop(id={self.id}, phone={self.phone}, email={self.email}, address_line_one={self.address_line_one},' \
               f'address_line_two={self.address_line_two}, city={self.city}, country={self.country} )'