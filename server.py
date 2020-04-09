from bottle import route
from bottle import run
from bottle import HTTPError
from bottle import request

from album import *
from html_pattern import AlbumsPage


@route('/albums/<artist>')
def albums(artist):
    album_list = find(artist)
    if not album_list:
        return HTTPError(404,  f'No results for artist: {artist}')
    message = f'{len(album_list)} found for artist: {artist}'
    page = AlbumsPage(artist=artist, albums=album_list)
    return page.render()


@route('/albums', method='POST')
def new_album():
    album_data = {
        'artist': request.forms.get('artist'),
        'album': request.forms.get('album'),
        'genre': request.forms.get('genre')
    }
    try:
        year = int(request.forms.get('year'))
    except ValueError:
        return HTTPError(400, '`year` must be a number')
    else:
        album_data['year'] = year
    err = check(album_data)
    if err:
        return err
    save_album(album_data)
    return f'Data saved: {album_data}'


def check(album_data):
    '''Validates the date. Checks if such a record exists.'''
    if album_data['year'] < 1900 or album_data['year'] > 3000:
        return HTTPError(409, 'Invalid date')
    session = connect_db()
    album = session.query(Album).filter(
        func.lower(Album.album) == album_data['album'].lower(), func.lower(Album.artist) ==
        album_data['artist'].lower()).first()
    print(Album.artist, album_data['artist'])
    if album:
        return HTTPError(409, f'[{album.artist}: {album.album}] - already in the database')
    return False


def save_album(album_data):
    session = connect_db()
    album = Album(**album_data)
    session.add(album)
    session.commit()


if __name__ == '__main__':
    run(host='127.0.0.1', port=8080, debug=True)
