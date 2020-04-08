class AlbumsPage:
    '''Wraps albums data in a html table'''

    def __init__(self, artist, albums):
        self.artist = artist.title()
        self.albums = albums
        self.content = ''
        # concatenate table rows from all albums into one string
        for album in albums:
            self.content += album.html()

    def render(self):
        pattern = f'''<!DOCTYPE html>
        <html lang="en" dir="ltr">
        <head>
            <meta charset="utf-8">
            <title>Search results for: {self.artist}</title>
        </head>
        <body>
            <h1>{self.artist}</h1>
            <table style="min-width: 600px;">
                <thead style="text-align:left">
                    <tr>
                        <th>album</th>
                        <th>genre</th>
                        <th>year</th>
                    </tr>
                </thead>
                <tbody>
                    {self.content}
                </tbody>
            </table>
            <br>
            <i>(total albums: {len(self.albums)})</i>
        </body>
        </html>'''
        return pattern
