import requests
from bs4 import BeautifulSoup

def bandcampscrape(url, comp):
    """
    Input: url with http:// or https:// included from bandcamp or based
    on bandcamp. Also asks if the album includes various artists (y/n).
        
    Returns a csv file that includes the artist name, the album name, 
    the day, month, and year of the release, the city, country, and 
    musical genre of the artist. All in a line for each track including
    the previous information as well as track number, title, 
    part (empty), part name (empty), length, minutes (empty), 
    seconds (empty), and the artist of the track in the case of a 
    compilation.
        
    Notes:
        1. Since csv files are comma-delimited, all commas in text 
        strings have been replaced with "|".
        2. If the artist name has a " - " string inside it, it will be
        exported erroneously since " - " marks the split between artist 
        and track title in bandcamp's formatting.
    """
            
    filename = "album_info.csv"
    
    f = open(filename, "w", encoding="utf-8")
    
    HEADERS = ("artist,album,day,month,year,city,country,disc,track,title,\
    part,name,length,min,sec,track_artist\n")
    
    f.write(HEADERS)
    
    r = requests.get(url)
    
    soup = BeautifulSoup(r.text,"html.parser")
    
    artist = soup.find("span",itemprop="byArtist").a.text
    
    album = soup.find(class_="trackTitle",itemprop="name").text.strip()
            
    reltemp = (soup.find(class_="tralbumData tralbum-credits").
               text.strip().split("\n")[0])
    
    released = reltemp[9:len(reltemp)].replace(",","")
        
    reldate = released.split(" ")
    
    day = reldate[1]
    
    months = {
            "January":1,
            "February":2,
            "March":3,
            "April":4,
            "May":5,
            "June":6,
            "July":7,
            "August":8,
            "September":9,
            "October":10,
            "November":11,
            "December":12
            }
    
    month = str(months[reldate[0]])
    
    year = reldate[2]
        
    location = soup.find(class_="location secondaryText").text.split(", ")
        
    if len(location) != 0:
        
        if len(location) == 1:
            
            city = ""
            
            country = location[0]
                                
        else:
        
            city = location[0]
                            
            country = location[1]
        
    else:
        city = ""
        
        country = ""
            
    if country == "":
    
        tags = (soup.find(class_="tralbumData tralbum-tags tralbum-tags-nu hidden").
                find_all(class_="tag"))
    
        country = tags[len(tags)-1].text
        
    else:
        
        country = country
    
    songlist = (soup.find(class_="track_list track_table").
                find_all(itemprop="tracks"))
            
    forlist = []
            
    for song in songlist:
    
        songno = song.find(class_="track_number secondaryText").text
        
        songtit = song.find(itemprop="name").text
                
        if comp == "y":
        
            trarttit = songtit.split(" - ", 1)
                        
            trtitart = trarttit[::-1]
            
            trart = trtitart[1]
                        
            trtit = trtitart[0]
            
        else:
            trtit = songtit
                        
            trart = ""
        
        try:
        
            songlen = song.find(class_="time secondaryText").text.strip()
            
        except AttributeError:
            
            songlen = ""
                
        songtup = (artist,album,released,city,country,songno,songtit,songlen)
    
        forlist.append(songtup)
        
        f.write(artist.replace(",","|") + "," +
                album.replace(",","|") + "," +
                day + "," +
                month + "," +
                year + "," +
                city + "," +
                country + "," +
                "1" + "," +
                songno + "," +
                trtit.replace(",","|") + "," + 
                "" + "," + 
                "" + "," +
                songlen + "," + 
                "" + "," + 
                "" + "," + 
                "" +
                trarbt.replace(",","|") +
                "\n")
                
    f.write(artist.replace(",","|") + "," +
            album.replace(",","|") + "," +
            day + "," +
            month + "," +
            year + "," +
            city + "," +
            country + "," +
            "" + "," +
            "" + "," +
            "" + "," +
            "" + "," +
            "" + "," +
            "" + "," +
            "" + "," +
            "" + "," +
            "" +
            "" +
            "\n")
    
    f.write(artist.replace(",","|") + "," +
            album.replace(",","|") + "," +
            day + "," +
            month + "," +
            year + "," +
            city + "," +
            country + "," +
            "1" + "," +
            "" + "," +
            "" + "," +
            "" + "," +
            "" + "," +
            "" + "," +
            "" + "," +
            "" + "," +
            ""+
            ""+
            "\n")
    
    f.close()
    
    return f

url = input("Enter url: ")
comp = input("Is it a multi-artist release? (y/n): ")
bandcampscrape(url, comp)