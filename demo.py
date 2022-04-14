
import json
import requests

def lyrics_finder():
    '''
    TODO:
    Leverage Musixmatch API to create an interactive CLI app that allows the user to key in
    a search query of a song. If the song is found on Musixmatch database, please display
    the lyrics to the user.
    Give the user a menu where they can choose to search or view saved song lyrics.
    You can ask a user whether they want to save their search results. If so, store the lyrics
    in a local SQLite database.
    '''

    song_id = input("Enter the ID of the song: ")
    #call  the api.ini file to use the api-key on the headers
    rr = requests.get(f"https://api.musixmatch.com/ws/1.1/track.lyrics.get?track_id={song_id}", headers=headers)
    return json.loads(rr.text)

print(lyrics_finder())