# This is really lazy, I'm not doing any sanitization here. I will clean the data with a script later
import sys
import requests
import pymongo

GENIUS_TOKEN = "ysipX1n9XQ1YwaySUTE3614Km-98YfPV8l9Ef6DptMV1u2YrYRMG6J-EXw-c0KrV"

client = pymongo.MongoClient()
db = client.databased

start = int(sys.argv[1])
end = int(sys.argv[2])

genius_url_1 = "http://api.genius.com/artists/"
genius_url_2 = "/songs?sort=popularity&per_page=50"
artists = db.artists.find()[start:end]
total = end - start
count = 0

for artist in artists:
  count = count + 1
  print "\n" + str(count) + "/" + str(total) + " "  + artist['name']
  print "Songs:"
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
      song['genius_primary_artist'] = raw_song['primary_artist']
      db.songs.insert(song)
      print song['title'] + " ",

