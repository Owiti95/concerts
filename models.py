from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Band(Base):
    __tablename__ = 'bands'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hometown = Column(String, nullable=False)

    concerts = relationship("Concert", back_populates="band")

    def venues(self):
        return {concert.venue for concert in self.concerts}

    def all_introductions(self):
        return [f"Hello {concert.venue.city}!!!!! We are {self.name} and we're from {self.hometown}" for concert in self.concerts]

    @classmethod
    def most_performances(cls, session):
        from sqlalchemy import func
        return session.query(cls).join(Concert).group_by(cls.id).order_by(func.count(Concert.id).desc()).first()

class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    city = Column(String, nullable=False)

    concerts = relationship("Concert", back_populates="venue")

    def bands(self):
        return {concert.band for concert in self.concerts}

    def concert_on(self, date, session):
        return session.query(Concert).filter_by(venue_id=self.id, date=date).first()

    def most_frequent_band(self, session):
        from sqlalchemy import func
        return session.query(Band).join(Concert).filter(Concert.venue_id == self.id).group_by(Band.id).order_by(func.count(Concert.id).desc()).first()

class Concert(Base):
    __tablename__ = 'concerts'

    id = Column(Integer, primary_key=True)
    band_id = Column(Integer, ForeignKey('bands.id'), nullable=False)
    venue_id = Column(Integer, ForeignKey('venues.id'), nullable=False)
    date = Column(Date, nullable=False)

    band = relationship("Band", back_populates="concerts")
    venue = relationship("Venue", back_populates="concerts")

    def hometown_show(self):
        return self.venue.city == self.band.hometown

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"