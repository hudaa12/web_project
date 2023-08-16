from lib.artist_repository import ArtistRepository
from lib.artist import Artist

"""
When we call Artistrepository #all
we get a list of Book objects reflecting the seed data.
"""

def test_get_all_artists(db_connection):
    db_connection.seed("seeds/artists.sql")
    repository = ArtistRepository(db_connection)

    artists = repository.all()

    assert artists == [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "ABBA", "Pop"),
        Artist(3, "Taylor Swift", "Pop"),
        Artist(4, "Nina Simone", "Jazz"),
        Artist(5, "Wild nothing", "Indie"),
    ]



def test_create(db_connection):
    db_connection.seed("seeds/artists.sql")
    repository = ArtistRepository(db_connection)
    artist = Artist(None, "Wild nothing", "Indie")
    repository.create(artist)
    assert repository.all() == [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "ABBA", "Pop"),
        Artist(3, "Taylor Swift", "Pop"),
        Artist(4, "Nina Simone", "Jazz"),
        Artist(5, "Wild nothing", "Indie"),
        Artist(6, "Wild nothing", "Indie"),
        ]