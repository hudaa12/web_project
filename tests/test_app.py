import pytest
import json
from playwright.sync_api import Page, expect

def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/albums.sql")
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Album(1, 1989, 2014, 1)\n" \
        "Album(2, Voyage, 2022, 2)"


def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/albums.sql")
    post_response = web_client.post("/albums", data={
        'title': 'Test title',
        'release_year': '1000',
        'artist_id': '1'
    })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""
    
    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, 1989, 2014, 1)\n" \
        "Album(2, Voyage, 2022, 2)\n" \
        "Album(3, Test title, 1000, 1)"


def test_post_albums_with_no_data(db_connection, web_client):
    db_connection.seed("seeds/albums.sql")
    post_response = web_client.post("/albums")
    assert post_response.status_code == 400
    assert post_response.data.decode('utf-8') == "" \
        "You need to submit a title, release_year, and artist_id"
    
    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, 1989, 2014, 1)\n" \
        "Album(2, Voyage, 2022, 2)"
    

    """
    GET /artists 
    Expected response (200 OK)
    """

def test_get_artists(db_connection, web_client):
    db_connection.seed("seeds/artists.sql")
    response = web_client.get("artists")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
    "Artist(1, Pixies, Rock)\n" \
    "Artist(2, ABBA, Pop)\n" \
    "Artist(3, Taylor Swift, Pop)\n" \
    "Artist(4, Nina Simone, Jazz)\n" \
    "Artist(5, Wild nothing, Indie)"


    """
    POST /artists
    create a new artist in the database
    """

def test_create_new_artist(db_connection, web_client):
    db_connection.seed("seeds/artists.sql")
    response = web_client.post('/artists')
    assert response.status_code == 200


def test_get_artists_include_new_artist(db_connection, web_client):
    db_connection.seed("seeds/artists.sql")
    response = web_client.get('/artists')

    assert response.status_code ==  200
    assert response.data.decode('utf-8') == "" \
    "Artist(1, Pixies, Rock)\n" \
    "Artist(2, ABBA, Pop)\n" \
    "Artist(3, Taylor Swift, Pop)\n" \
    "Artist(4, Nina Simone, Jazz)\n" \
    "Artist(5, Wild nothing, Indie)"



def test_get_artists(page, test_web_address):
    page.goto(f"http://{test_web_address}/Taylor Swift")
    strong_tag = page.locator("strong")
    expect(strong_tag).to_have_text("Taylor Swift")