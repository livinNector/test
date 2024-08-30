# prompt: use sqlalchemy to create a database and tables for the above superhero class
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker



engine = create_engine('sqlite:///:sample.db', echo=False)
Base = declarative_base()

class Superhero(Base):
  __tablename__ = 'superheroes'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  power = Column(String)
  weakness = Column(String)
  nemisis = Column(String)
  strength = Column(Integer)
  weapon = Column(String)
  is_strong = Column(Boolean)

  def __repr__(self):
    return "<Superhero(name='%s', power='%s', weakness='%s', nemisis='%s', strength='%s', weapon='%s', is_strong='%s')>" % (
                          self.name, self.power, self.weakness, self.nemisis, self.strength, self.weapon, self.is_strong)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

hero1 = Superhero(name='deadpool',power='regeneration',weakness='attitude',nemisis=None,strength=80,weapon='swords',is_strong=True)
hero2 = Superhero(name='hawkeye',power=None,weakness='human',nemisis='Thanos',strength=40,weapon='bow and arrow',is_strong=False)
hero3 = Superhero(name = "batman",power=None,weakness = "human",nemisis = 'atittude',strength = 50,weapon = 'bat wing',is_strong=False)
session.add(hero1)
session.add(hero2)

session.commit()

superheros=session.query(Superhero).all()
