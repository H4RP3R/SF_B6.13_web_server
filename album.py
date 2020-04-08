import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func


DB_PATH = 'sqlite:///albums.sqlite3'
Base = declarative_base()


class Album(Base):
    '''Describes the structure of the "album" table for storing a music collection.'''

    __tablename__ = 'album'

    id = sa.Column(sa.INTEGER, primary_key=True)
    year = sa.Column(sa.INTEGER)
    artist = sa.Column(sa.TEXT)
    genre = sa.Column(sa.TEXT)
    album = sa.Column(sa.TEXT)

    def html(self):
        # insert data into a table row
        text = f'<tr><td>{self.album}</td><td>{self.genre}</td><td>{self.year}</td></tr>'
        return text


def connect_db():
    '''Creates a database connection. Returns the session object.'''
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()


def find(artist):
    '''Finds all albums in db by artist name.'''
    session = connect_db()
    albums = session.query(Album).filter(func.lower(Album.artist) == artist.lower()).all()
    return albums
