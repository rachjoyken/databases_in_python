from lib.album import Album

"""
Constructs with
id, title, release_year, and artist_id
"""

def test_constructs_with_fields():
    album = Album(1, "Dark Side", 1995, 2)
    assert album.id == 1
    assert album.title == "Dark Side"
    assert album.release_year == 1995
    assert album.artist_id == 2

"""
We can compare two identical albums
And have them be equal
"""
def test_albums_are_equal():
    album_1 = Album(1, "Dark Side", 1995, 2)
    album_2 = Album(1, "Dark Side", 1995, 2)
    assert album_1 == album_2    

"""
We can format albums to strings nicely
"""

def test_albums_format_nicely():
    album = Album(1, "Dark Side", 1995, 2)
    assert str(album) == "Album(1, Dark Side, 1995, 2)"
      


    
