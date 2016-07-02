DataBased - A Hip-Hop Data Set
==============================
These are scripts to scrape your own hip-hop dataset, to be used for machine learning, statistics, or reference. Soon I will post .json files, so you will not have to build the data set yourself. To build the dataset in MongoDB, execute the scripts in this order:
- artist_finder.py
  - Run this script with 2 arguments: The seed artist, and the time limit in seconds.
  - e.g. `python artist_finder.py Kanye 100`
- genius_id_scraper.py
  - Simply run this script, and wait until it has completed. It might take a while, since it has to keep downloading full HTML pages (I think that slows it down). The Genius API doesn't really have a great way for getting artist IDs, because if you search for an artist name it only returns a list of songs, and the artist you're searching for might not actually be listed as the primary artist for the first song in the list and then you run into all kinds of problems. When the script has run its course, you now have all the genius IDs for the artists! (I hope)

- song_scraper_genius.py
  - Run this script to create a collection "songs". This will not have lyrics, lastfm tags, or spotify audio features.
  - Run with 2 arguments: the index of the first artist in the collection you want to start with, and the (index + 1) of the last artist you want in the interval
  - e.g. `python song_scraper_genius.py 0 300` followed by `python song_scraper_genius 300 600` etc... until you are done or satisfied.

- lyrics_scraper.py
  - run this script to create a collection "lyrics". This script works the same way as song_scraper_genius.py, where you must run the script with 2 arguments. Again, you can run from 0 to (end), or you can split this up into parts. (You can even run multiple processes on different intervals if you're feeling fancy.) This script doesn't use API calls so you won't be throttled, but since you'll be downloading HTML pages it will be very slow.
  
Instead of running the scripts yourself, feel free to use the .json files to populate your database. To generate artists.json I ran artist_finder.py for 30 minutes, using the seed "Kanye", followed by running genius_id_scraper.py. To generate songs.json I ran song_scraper_genius.py from 0 to 16901.
