DataBased - A Hip-Hop Data Set
==============================
These are scripts to scrape your own hip-hop dataset, to be used for machine learning, statistics, or reference. If you do not want to build the set yourself, the exported collections can be found in JSON format in the `Raw_JSON` archive. To build the set in MongoDB, see the instructions in INSTRUCTIONS.md

#Schema
- Artists
  - genres (array of strings)
  - related artists (array of artists with genres, names, spotify info) (max 20)
  - Spotify ID (as "id")
  - ID on Genius
  - last.fm tags (count, url to tag, tag name)

- Songs
  - title
  - url to lyrics on Genius
  - Genius name of artist associated with song
  - Genius ID of song

- Lyrics
  - Genius ID of song
  - text
  - title of song

# Goodies


#TO-DO:
  - Document schema in README
  - Scrape audio-features for songs from spotify
  - Run my own analytics, including:
    - swearing metrics for songs/artists
    - unique word counts for artists for set lyric set size
    - references to places
    - etc...
