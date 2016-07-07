DataBased - A Hip-Hop Data Set
==============================
These are scripts to scrape your own hip-hop dataset, to be used for machine learning, statistics, or reference. If you do not want to build the set yourself, the exported collections can be found in JSON format in the `Raw_JSON` archive. To build the dataset in MongoDB, execute the scripts in this order:
- artist_finder.py
  - Run this script with 2 arguments: The seed artist, and the time limit in seconds.
  - e.g. `python artist_finder.py Kanye 100`

- batch_genius_id_scraper.py
  - Simply run this script with 2 arguments (the size of your collection and the number of processes you desire), and wait until it has completed. It might take a while, since it has to keep downloading full HTML pages (I think that slows it down). The Genius API doesn't really have a great way for getting artist IDs, because if you search for an artist name it only returns a list of songs, and the artist you're searching for might not actually be listed as the primary artist for the first song in the list and then you run into all kinds of problems. When the script has run its course, you now have all the genius IDs for the artists! (I hope)

- song_scraper_genius.py
  - Run this script to create a collection "songs". This will not have lyrics, lastfm tags, or spotify audio features.
  - Run with 2 arguments: the index of the first artist in the collection you want to start with, and the (index + 1) of the last artist you want in the interval
  - e.g. `python song_scraper_genius.py 0 300` followed by `python song_scraper_genius 300 600` etc... until you are done or satisfied.

- batch_lyrics_scraper
  - Run with 2 arguments: the size of your songs collection and the number of python processes you'd like to run. The higher the number of processes the faster this thing will run, but it'll seriously cripple you while it runs.
  - e.g. `./batch_lyrics_scraper 365344 100`
  - The output is at the moment is a mess of song IDs and titles. But it gives you a bit of an idea of how far along you are.
  - I am running this with 100 processes on my MacBook Pro, and all 4 cores are maxed out at the moment.
  - NOTE: You might find that some of the processes just end up hanging (or db.lyrics.count() doesn't equal db.songs.count()), but I don't think that's a huge problem. Just run the script again, and it should sort itself out. It avoids inserting duplicates, so you shouldn't end up with any problems if you run this multiple times.

Instead of running the scripts yourself, feel free to use the `.json` files in the `Raw_JSON` archive to populate your database. To generate `artists.json` I ran `artist_finder.py` for 30 minutes, using the seed `"Kanye"`, followed by running `genius_id_scraper.py`. To generate `songs.json` I ran `song_scraper_genius.py` from 0 to 16901.
