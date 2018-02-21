# bandcamp_webscrape
webscraper to gather information from bandcamp album pages in a csv file

I keep track of the albums I listen to with an excel file.

To make things easier, I wrote this code to fetch the data I need from the bandcamp page of the release.

Therefore, the formatting of the csv output file is related to the formatting of my excel spreadsheet. Feel free to take the code and modify it for your needs.

Most useful and standardized data that can be gathered from bandcamp is used:

-artist name

-album title

-release date (one column for date, one for month (1-12), and one for year)

-city 

-country (or state/province for certain countries)

-track number

-track title

-track length (00:00 format)

-track artist (if multi-artist release)

I also left some space for non-standardized information, which can be added manually if desired:

-multi-track compositions:

-movement number 

-movement name

-duration information:

--seconds (which I use to transform 00:00 time format to total amount of seconds)

--minutes (which I use to transform total amount of seconds to decimal minutes format)

There are also two more rows than necessary being printed, they don't contain track information. I use the first one to summarize all the track lengths on excel, and the second one I cut to another sheet.
