# cricketbattingStats
Analysis of batting averages

One of my major passions in life is cricket. After taking Prof. Martyn Plummer's course at the University of Warwick on Linear Statistical Modelling and having attended a few
talks sponsored by the Warwick Statistics Society that mentioned random forests, I was inspired to create a predictive model for batting averages using both random forests and
linear models.

The first challenge was extracting the data from ESPNCricInfo's StatsGuru search. This was done by looking at the relevant HTML source pages and looking for link patterns.
Some features weren't available directly on the database, so I had to encorporate in my Python code the ability to go to each individual player page and look for those features. 
One example of such a feature is whether or not a player is left or right handed.

My code that extracts this dataset from the internet has already been uploaded. I have built a few random forest machine learning models as well as linear models to predict
cricketers' batting averages. These will be uploaded in time, once I am happy to publish them!
