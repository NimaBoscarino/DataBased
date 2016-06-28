import requests
import sys
from lxml import html
import re

GENIUS_URL = "http://www.genius.com/artists/"
artist = sys.argv[1]

artist_genius_response = requests.get(GENIUS_URL + artist)
tree = html.fromstring(artist_genius_response.content)
genius_id_raw = tree.xpath('//form[@class="edit_artist"]/@action')[0]
m = re.search('/artists/(.+)', genius_id_raw)
if m:
  genius_id = m.group(1)
print genius_id
