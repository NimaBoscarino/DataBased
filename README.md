DataBased - A Hip-Hop Database
==============================
These are scripts to scrape your own hip-hop dataset, to be used for machine learning, statistics, or reference. Soon I will post .csv files, so you will not have to build the data set yourself. To build the dataset in MongoDB, execute the scripts in this order:
- artist_finder.py
  - Run this script with 2 arguments: The seed artist, and the time limit in seconds.
  - e.g. `python artist_finder.py Kanye 100`

Instead of running the script yourself, feel free to use the .json files to populate your database. To generate artists.json I ran artist_finder.py for 30 minutes, using the seed "Kanye".
