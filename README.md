DataBased - A Hip-Hop Data Set
==============================
These are scripts to scrape your own hip-hop dataset, to be used for machine learning, statistics, or reference. Soon I will post .json files, so you will not have to build the data set yourself. To build the dataset in MongoDB, execute the scripts in this order:
- artist_finder.py
  - Run this script with 2 arguments: The seed artist, and the time limit in seconds.
  - e.g. `python artist_finder.py Kanye 100`
- genius_id_scraper.py
  - Simply run this script, and wait until it has completed. It might take a while, since it has to keep downloading full HTML pages (I think that slows it down). The Genius API doesn't really have a great way for getting artist IDs, because if you search for an artist name it only returns a list of songs, and the artist you're searching for might not actually be listed as the primary artist for the first song in the list and then you run into all kinds of problems. When the script has run its course, you now have all the genius IDs for the artists! (I hope)

Instead of running the scripts yourself, feel free to use the .json files to populate your database. To generate artists.json I ran artist_finder.py for 30 minutes, using the seed "Kanye", followed by running genius_id_scraper.
