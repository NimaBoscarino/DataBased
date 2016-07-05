import sys
import requests
import pymongo
from lxml import html

GENIUS_TOKEN = "ysipX1n9XQ1YwaySUTE3614Km-98YfPV8l9Ef6DptMV1u2YrYRMG6J-EXw-c0KrV"

client = pymongo.MongoClient()
db = client.databased

start = int(sys.argv[1])
end = int(sys.argv[2])
LASTFM_TOKEN = "1a5d9f463b5436185d117f273573a537"
genius_url_1 = "http://api.genius.com/artists/"
genius_url_2 = "/songs?sort=popularity&per_page=50"
artists = db.artists.find()[start:end]
total = end - start
count = 0

for artist in artists:
  count = count + 1
  print str(count) + "/" + str(total) + " "  + artist['name']
  top_songs = requests.get( genius_url_1 + str(artist['genius_id']) + genius_url_2,
      params={"access_token":GENIUS_TOKEN}
      ).json()['response']['songs']
  for raw_song in top_songs:
    if db.songs.count({"genius_id":raw_song['id']}) == 0:
      song = {}
      song['title'] = raw_song['title']
      song['genius_id'] = raw_song['id']
      song['full_title'] = raw_song['full_title']
      song['lyrics_url'] = raw_song['url']
      #tags
      primary_artist = raw_song['primary_artist']['name']
      #tag_request_url = 'http://ws.audioscrobbler.com/2.0/?method=track.gettoptags&autocorrect=1&track=' + song['title'] + '&artist=' + primary_artist + '&api_key=' + LASTFM_TOKEN
      #song_tag_request = requests.get(tag_request_url)
      #tree = html.fromstring(song_tag_request.content)
      #tags = tree.xpath('//lfm/toptags/tag[count > 3]/name/text()')
      #song['tags'] = tags
      #artists
      #url_song_title = song['title'].replace("%", "%25")
      #spotify_url_1 = 'https://api.spotify.com/v1/search?type=track&q=' + primary_artist + ' ' + url_song_title
      #song_info_response = requests.get(spotify_url_1)
      #song_info_request = song_info_response.json()
      song['genius_artist'] = primary_artist
      #if len(song_info_request['tracks']['items']) != 0:
      #  song['artists'] = song_info_request['tracks']['items'][0]['artists']
      db.songs.insert(song)
