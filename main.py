import scrape #extrracts the data from the internet
import clean #cleans up data to make analysis possible

def __main__():
    headers, playerstats = scrape.extract() # Extracts the field labels as well as each record
    scrape.writetocsv(headers,playerstats) # writes data to the csv
    clean.edit() #cleans up data to make analysis possible
__main__()
