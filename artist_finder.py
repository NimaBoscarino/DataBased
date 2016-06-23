#
# This script finds a bunch of artists, but does not gather additional information.
# It is just to begin populating the artists collection with meaningful data
#

import requests
import sys
import pymongo
from collections import deque
import time
import re
import dpath.util

LASTFM_TOKEN = "1a5d9f463b5436185d117f273573a537"
GENIUS_TOKEN = "ysipX1n9XQ1YwaySUTE3614Km-98YfPV8l9Ef6DptMV1u2YrYRMG6J-EXw-c0KrV"
search_url = "https://api.spotify.com/v1/search"
related_url_1 = "https://api.spotify.com/v1/artists/"
related_url_2 = "/related-artists"
last_fm_url = "http://ws.audioscrobbler.com/2.0/?method=artist.gettoptags&artist="
artist_queue = deque([])

client = pymongo.MongoClient()
db = client.databased

seed_artist = sys.argv[1] # be reasonable with your seed. I'm picking Kanye as my first.
start_time = time.time() # this tree goes on forever. I'm setting time as my halting condition now
time_limit = int(sys.argv[2])
tally = 0

find_seed_response = requests.get( search_url,
    params = { "q" : seed_artist, "type" : "artist" , "limit" : 1})

seed_artist = find_seed_response.json()['artists']['items'][0]
artist_queue.append(seed_artist)

while (time.time() - start_time < time_limit) and len(artist_queue) > 0:
  artist = artist_queue.popleft()
  tag_request = requests.get( last_fm_url + artist['name'] + "&api_key=" + LASTFM_TOKEN + "&format=json")
  try:
    tags = tag_request.json()['toptags']['tag']
  except:
    tags = []
  hiphop_count = 0
  pattern = re.compile('(?i)hip[ -]*hop')
  for tag in tags:
    if pattern.match(tag['name']):
        hiphop_count = hiphop_count + tag['count']

  if hiphop_count > 5 and db.artists.count({"name": artist['name']}) == 0 and artist['followers']['total'] > 2500: #tune to your liking
    related_artists_response = requests.get( related_url_1 + artist['id'] + related_url_2 )
    related_artists = related_artists_response.json()['artists']
    artist['related_artists'] = related_artists # might be neat for graphing closeness of artists...
    db.artists.insert(artist)
    tally = tally + 1
    print str(tally) + " " + artist['name']
    for related in related_artists:
      if related not in artist_queue: # really cuts down the number of artists in the list, but it will probably slow the thing down a bit/lot
        artist_queue.append(related) # I really hope I don't blow out the list....

  if (tally%20 == 0):
    print str(int(time_limit - (time.time() - start_time))) + " seconds remaining, " + str(len(artist_queue)) + " artists currently queued."
if len(artist_queue) == 0:
  print "Queue is empty! Number of artists inserted is: " + str(tally) + "."
else:
  print "Out of time! Number of artists inserted is: " + str(tally) + "."

print "If you would want more artists, pick a new seed!"
