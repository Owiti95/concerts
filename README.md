# Concert Domain Project

## Overview

This project models a concert domain using SQLAlchemy to define the relationships between bands, venues, and concerts. It allows for querying and manipulation of data in a relational database. The project follows a simple structure with three primary models: `Band`, `Venue`, and `Concert`, each representing key entities in the concert ecosystem.

## Models

### 1. Band

**Attributes:**
- `id`: Integer, primary key
- `name`: String, the name of the band
- `hometown`: String, the city the band is originally from

**Relationships:**
- A band can have multiple concerts (`concerts` relationship).
  
**Methods:**
- `venues()`: Returns a set of unique venues where the band has performed.
- `all_introductions()`: Returns a list of introduction strings for each concert.
- `most_performances(session)`: Class method that returns the band with the most concerts.
- `play_in_venue(venue, date)`: Creates a new concert for the band at the specified venue and date.

### 2. Venue

**Attributes:**
- `id`: Integer, primary key
- `title`: String, the name of the venue
- `city`: String, the city where the venue is located

**Relationships:**
- A venue can host multiple concerts (`concerts` relationship).

**Methods:**
- `bands()`: Returns a set of unique bands that have performed at the venue.
- `concert_on(date, session)`: Returns the first concert on the specified date at the venue.
- `most_frequent_band(session)`: Returns the band with the most concerts at the venue.

### 3. Concert

**Attributes:**
- `id`: Integer, primary key
- `band_id`: ForeignKey to `bands.id`
- `venue_id`: ForeignKey to `venues.id`
- `date`: String, the date of the concert

**Relationships:**
- Each concert belongs to a specific band (`band` relationship) and a venue (`venue` relationship).

**Methods:**
- `hometown_show()`: Returns `True` if the concert is in the band's hometown; otherwise, returns `False`.
- `introduction()`: Returns a formatted string introducing the band at the concert venue.

## Database Setup

The project uses SQLite as the database backend, and SQLAlchemy handles the ORM functionality. 

### Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd concerts
   ```

2. **Install Dependencies:**
   Ensure you have Python and pip installed. Install the required packages:
   ```bash
   pip install sqlalchemy
   ```

### Database Initialization

To initialize the database and create the necessary tables:

1. Open a Python shell or create a script.
2. Use the following code to create the database and tables:
   ```python
   from sqlalchemy import create_engine
   from models import Base

   engine = create_engine('sqlite:///concerts.db')
   Base.metadata.create_all(engine)
   ```

## Sample Data Insertion

To insert sample data into the database, use the provided `insert_sample_data` function:

```python
from sqlalchemy.orm import sessionmaker
from models import Band, Venue, Concert, insert_sample_data
from database import Database  # Assuming your Database class is in database.py

database = Database()
session = database.get_session()

insert_sample_data(session)
```

## Querying Data

Once your data is set up, you can start querying:

```python
# Query all concerts
for concert in session.query(Concert).all():
    print(f"Concert: {concert.band.name} at {concert.venue.title} on {concert.date}")

# Find a band's venues
band = session.query(Band).first()
print(band.venues())

# Find the most frequent band at a venue
venue = session.query(Venue).first()
print(venue.most_frequent_band(session))
```

## Logging

The project includes logging for monitoring operations. Ensure that logging is set up at the start of your main program:

```python
import logging

logging.basicConfig(level=logging.INFO)
```

## Conclusion

This project provides a foundational structure for managing concerts, bands, and venues using SQLAlchemy. You can extend the models and methods further to accommodate additional requirements as needed.
