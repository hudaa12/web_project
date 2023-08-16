from lib.artist import Artist

def test_artist_constructs():
    artist = Artist(1, "Test name", "Test genre")
    assert artist.id == 1
    assert artist.name == "Test name"
    assert artist.genre == "Test genre"


def test_artist_nicely():
    artist = Artist(1, "Test name", "Test genre")
    assert str(artist) == "Artist(1, Test name, Test genre)"


def test_artist_are_equal():
    artist1 = Artist(1, "Test name", "Test genre")
    artist2 = Artist(1, "Test name", "Test genre")
    assert artist1 == artist2