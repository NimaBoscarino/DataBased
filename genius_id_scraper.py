import pymongo
import requests
import sys
from lxml import html
import re

client = pymongo.MongoClient()
db = client.databased

GENIUS_URL = "http://www.genius.com/artists/"

artists = db.artists.find()

for artist in artists:
  print artist['name']
  artist_name = artist['name'].replace('.', '')
  artist_genius_response = requests.get(GENIUS_URL + artist_name)
  tree = html.fromstring(artist_genius_response.content)
  genius_id_raw = tree.xpath('//form[@class="edit_artist"]/@action')[0]
  m = re.search('/artists/(.+)', genius_id_raw)
  if m:
    genius_id = m.group(1)
  result = db.artists.update_one(
    {"id": artist['id']},
      {"$set": {"genius_id": int(genius_id)}}
    )
  print genius_id
