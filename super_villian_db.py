from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set up the database engine and base class
engine = create_engine('sqlite:///sample.db', echo=False)  # Updated to correct the SQLite URL format
Base = declarative_base()

# Define the Supervillain class
class Supervillain(Base):
    __tablename__ = 'supervillains'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    power = Column(String)
    weakness = Column(String)
    nemesis = Column(String)
    strength = Column(Integer)
    weapon = Column(String)
    is_dangerous = Column(Boolean)

    def __repr__(self):
        return "<Supervillain(name='%s', power='%s', weakness='%s', nemesis='%s', strength='%s', weapon='%s', is_dangerous='%s')>" % (
            self.name, self.power, self.weakness, self.nemesis, self.strength, self.weapon, self.is_dangerous)

# Create all tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Insert some data into the supervillains table
villain1 = Supervillain(name='Loki', power='Illusion', weakness='Family', nemesis='Thor', strength=70, weapon='Scepter', is_dangerous=True)
villain2 = Supervillain(name='Thanos', power='Infinity Gauntlet', weakness='Overconfidence', nemesis='Avengers', strength=100, weapon='Gauntlet', is_dangerous=True)
villain3 = Supervillain(name='Joker', power='Chaos', weakness='Mental Instability', nemesis='Batman', strength=60, weapon='Various Gadgets', is_dangerous=True)

# Add and commit the new supervillains to the database
session.add(villain1)
session.add(villain2)
session.add(villain3)
session.commit()

# Query the supervillains
supervillains = session.query(Supervillain).all()

# Print out all supervillains
for villain in supervillains:
    print(villain)
