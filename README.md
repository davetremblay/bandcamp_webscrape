# bandcamp_webscrape
webscraper to gather information from bandcamp album pages in a csv file

I keep track of the albums I listen to with an excel file. 
To make things easier, I wrote this code to fetch the data I need from the bandcamp page of the release.
Therefore, the formatting of the csv output file is related to the formatting of my excel spreadsheet.
Most useful and standardized data that can be gathered from bandcamp is used:
  artist name
  album title
  release date
  city and country (or state for US states)
  track number
  track title
  track length
  track artist (for multi-artist releases)
I also left some space for non-standardized information, which can be added manually if desired:
  multi-track compositions:
    part number
    part name
  duration information:
    minutes (which I use to transform total amount of seconds to decimal minutes format)
    seconds (which I use to transform 00:00 time format to total amount of seconds)
