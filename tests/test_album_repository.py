from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When i get a call #all 
I get all the albums in the albums table
"""

def test_all(db_connection):
    db_connection.seed("seeds/albums.sql")
    repository = AlbumRepository(db_connection)
    assert repository.all() == [
        Album(1, "1989", 2014, 1),
        Album(2, 'Voyage', 2022, 2),
        ]
    

"""
When i call #create 
I create an album in the database
and I can see it back in #all
"""

def test_create(db_connection):
    db_connection.seed("seeds/albums.sql")
    repository = AlbumRepository(db_connection)
    album = Album(None, "Test Title", 1000, 3)
    repository.create(album)
    assert repository.all() == [
        Album(1, '1989', 2014, 1),
        Album(2, 'Voyage', 2022, 2),
        Album(3, 'Test Title', 1000, 3)
        ]