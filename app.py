import os
from lib.database_connection import get_flask_database_connection
from flask import Flask, request, render_template
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist import Artist
from lib.artist_repository import ArtistRepository

app = Flask(__name__)

@app.route('/albums', methods=['POST'])
def post_albums():
    if has_invalid_album_parameters(request.form):
        return "You need to submit a title, release_year, and artist_id", 400
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(
        None,
        request.form['title'],
        request.form['release_year'],
        request.form['artist_id'])
    repository.create(album)
    return '', 200


@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    return "\n".join(
        f"{album}" for album in repository.all()
    )

@app.route('/albums')
def has_invalid_album_parameters(form):
    return 'title' not in form or \
        'release_year' not in form \
        or 'artist_id' not in form


@app.route('/artists')
def get_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    return "\n".join(
        f"{artist}" for artist in repository.all()
    )

artists = ["Pixies", "ABBA", "Taylor Swift", "Nina Simone"]

@app.route('/artists', methods=['POST'])
def create_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    data = request.form
    name = data.get('name')
    genre = data.get('genre')

    artists.append(name)
    return '', 200


@app.route('/artists')
def get_artist():
    return render_template("Taylor Swift.html")




if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

