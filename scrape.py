import requests
from bs4 import BeautifulSoup
import csv

# Extract data from webpage and find the table in which all necessary data is required
def extract():
    i = 1 # page 1
    playerstats = [] # list containing each player record
    ''' we loop through each page that has data. Break only when no more data available'''
    while True: 
        website = requests.get("https://stats.espncricinfo.com/ci/engine/stats/index.html?class=1;page="+str(i)+";spanmin1=01+Jan+1986;spanval1=span;template=results;type=batting")
        soup = BeautifulSoup(website.content, 'lxml')
        # the data is contained in an html table with class engineTable. However, there are 4 such tables available
        # We are interested in the 3rd such table.
        contenttable = soup.findAll('table', attrs={'class':'engineTable'})
        data = contenttable[2]
        if i == 1:
            # Extract table headers.
            # Headers located in <tr> tag with class headlinks. Remove leading \n's, split into headers array
            headers = (data.find('tr', attrs={'class':'headlinks'})).text.strip().split("\n")
            headers.append("Batting Style")
            headers.append("Player Role")
        if data.text.find("No records available to match this query") == -1:
            # In this case, we have data available on the page
            # For each piece of player data, strip to remove trailing and leading whitespace and turn into an array
            # Then add to playerstats[]
            for j in data.findAll('tr', attrs={'class':'data1'}):
                info = (j.text.strip()).split("\n") # Gets player info as an array
                link = j.find("a", attrs={"class":"data-link"}) # Gets the latter part of the link to the player page
                playerpage = requests.get("https://stats.espncricinfo.com" + str(link.get("href"))) # Connects to the individual player page
                soup2 = BeautifulSoup(playerpage.content, 'lxml')
                playerbatstyle = soup2.find('b', string="Batting style").find_parent("p").find("span").text # Finds out whether or not a player is left or right handed
                try:
                    lhrs = playerbatstyle.lower()
                    if lhrs.find("right") != -1:
                        info.append("R")
                    else:
                        info.append("L")
                except IndexError:
                    info.append("-")

                # Now get the player's role in the team
                playerRole = soup2.find("b", string="Playing role")
                if playerRole != None:
                    playerRole = playerRole.find_parent("p").find("span").text
                    info.append(playerRole.lower())
                else:
                    info.append("")
                print(info[0])
                playerstats.append(info)
        else:
            break
        i += 1
    return headers, playerstats

def writetocsv(header, stats):
    # Open CSV file and write header to the CSV
    file = open('battingstats.csv', 'w')
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    # Write each player statistic to the CSV
    for i in stats:
        csvwriter.writerow(i)
    file.close()
    print("Done.")
