import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()

class User(Base):

	__tablename__ = "user"
	id = sa.Column(sa.INTEGER, primary_key=True)
	first_name = sa.Column(sa.TEXT)
	last_name = sa.Column(sa.TEXT)
	gender = sa.Column(sa.TEXT)
	email = sa.Column(sa.TEXT)
	birthdate = sa.Column(sa.TEXT)
	height = sa.Column(sa.REAL)

engine = sa.create_engine(DB_PATH)
Sessions = sessionmaker(engine)
session = Sessions()
users = session.query(User).all()

first_name = str(input('first_name: '))
last_name = str(input('last_name: '))
gender = str(input('gender: '))
email = str(input('email: '))
birthdate = str(input('birthdate: '))
height = float(input('height: '))
regist_user = User( 
	first_name=first_name, 
	last_name=last_name, 
	gender=gender, 
	email=email, 
	birthdate=birthdate, 
	height=height
	)

session.add(regist_user)
session.commit()