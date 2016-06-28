import pymongo
import requests
import sys
from lxml import html
import re

client = pymongo.MongoClient()
db = client.databased

GENIUS_URL = "http://www.genius.com/artists/"

artists = db.artists.find()
total = db.artists.count()
count = 0

for artist in artists:
  count = count + 1
  print artist['name']
  artist_name = artist['name'].replace('.', '')
  artist_genius_response = requests.get(GENIUS_URL + artist_name)
  if artist_genius_response.status_code == 200:
    tree = html.fromstring(artist_genius_response.content)
    genius_id_raw = tree.xpath('//form[@class="edit_artist"]/@action')[0]
    m = re.search('/artists/(.+)', genius_id_raw)
    if m:
      genius_id = m.group(1)
    db.artists.update_one(
      {"id": artist['id']},
        {"$set": {"genius_id": int(genius_id)}}
      )
    print str(count) + "/" + str(total) + "\t" + str(genius_id) + "\t" + artist['name']
  else: #dropping artists that can't be found on genius. They're probably not relevant anyways.
    db.artists.delete_one( {"id": artist['id']} )
    print str(count) + "/" + str(total) + "\t" + "DROPPED" + "\t" + artist['name']
