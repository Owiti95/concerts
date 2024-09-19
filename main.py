from database import Database
from models import Band, Venue, Concert
from datetime import date

def insert_sample_data(session):
    # Insert sample data
    band1 = Band(name='Westlife', hometown='Ireland')
    band2 = Band(name='Big Time Rush', hometown='USA')
    band3 = Band(name='Maverick City', hometown='UK')

    venue1 = Venue(title='Aviva Stadium', city='Ireland')
    venue2 = Venue(title='Madison Square Garden', city='New York')
    venue3 = Venue(title='Maverick City', city='UK')

    concert1 = Concert(band=band1, venue=venue1, date=date(2024, 10, 28))
    concert2 = Concert(band=band2, venue=venue2, date=date(2024, 9, 29))
    concert3 = Concert(band=band3, venue=venue3, date=date(2024, 11, 5))

    session.add_all([band1, band2, band3, venue1, venue2, venue3, concert1, concert2, concert3])
    session.commit()

def main():
    db = Database()
    session = db.get_session()

    # create sample data
    insert_sample_data(session)

    # queries
    for concert in session.query(Concert).all():
        print(f"Concert: {concert.band.name} at {concert.venue.title} on {concert.date}")

    # close the session
    session.close()

if __name__ == "__main__":
    main()
