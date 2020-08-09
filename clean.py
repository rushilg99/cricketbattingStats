import pandas as pd

def edit():
    '''rewrites the scraped data set to make analysis possible'''
    '''(1) Introduce column stating whether or not the highest score is out or not out'''
    dataset = pd.read_csv("battingstats.csv")
    hsloc = dataset.columns.get_loc("HS") # get location of the column titled "HS"
    notout_yesno = pd.Series([])

    for i in range(len(dataset)): #len(dataset) gives the number of rows
        if str(dataset["HS"][i]).find("*") != -1: 
            notout_yesno[i] = "Yes" 
            dataset["HS"][i] = dataset["HS"][i].replace("*", "") # remove the * indicating a not out
        else:
            notout_yesno[i] = "No"
    dataset.insert(hsloc+1,"HS-N/O?",notout_yesno) #insert the new column after the high score column
    '''(2) Rename column names'''
    dataset = dataset.rename(columns={"100":"Hundreds", "50":"Fifties", "0":"Ducks"})
    dataset.to_csv("battingstats.csv", index=False)
