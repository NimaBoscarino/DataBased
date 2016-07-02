import sys
import requests
import pymongo
from lxml import html

client = pymongo.MongoClient()
db = client.databased

start = int(sys.argv[1])
end = int(sys.argv[2])

songs = db.songs.find()[start:end]
total = end - start
count = 0

for song in songs:
  if db.lyrics.count({"genius_id":song['genius_id']:
    lyrics = {}
    lyrics['title'] = song['title']
    lyrics['genius_id'] = song['genius_id']
    count = count + 1
    print "\n" + str(count) + "/" + str(total) + " " + str(start + count - 1) + " " + song['title']
    lyrics_url = song['lyrics_url']
    r = requests.get(lyrics_url)
    tree = html.fromstring(r.content)
    raw_lyrics = tree.xpath('//lyrics//text()')
    lyrics['text'] = ''.join(raw_lyrics)
    db.lyrics.insert(lyrics)
