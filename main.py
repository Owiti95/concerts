from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Band, Venue, Concert
from datetime import date
import logging

def insert_sample_data(session):
    """Insert sample data into the database."""
    if session.query(Band).count() == 0 and session.query(Venue).count() == 0:
        band1 = Band(name='Sauti Sol', hometown='Kakamega')
        band2 = Band(name='Wakadinali', hometown='Nairobi')
        band3 = Band(name='Vijana Barubaru', hometown='Kisii')

        venue1 = Venue(title='Afraha Stadium', city='Nakuru')
        venue2 = Venue(title='Uhuru Gardens', city='Nairobi')
        venue3 = Venue(title='Mega City', city='Kisumu')

        concert1 = Concert(band=band1, venue=venue1, date=date(2024, 10, 28))
        concert2 = Concert(band=band2, venue=venue2, date=date(2024, 9, 29))
        concert3 = Concert(band=band3, venue=venue3, date=date(2024, 11, 5))

        session.add_all([band1, band2, band3, venue1, venue2, venue3, concert1, concert2, concert3])
        session.commit()
        logging.info("Sample data inserted.")
    else:
        logging.info("Sample data already exists.")

def main():
    # Create the database engine
    engine = create_engine('sqlite:///concerts.db')

    # Create all tables
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Insert sample data
    insert_sample_data(session)

    # Queries
    for concert in session.query(Concert).all():
        logging.info(f"Concert: {concert.band.name} at {concert.venue.title} on {concert.date}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
