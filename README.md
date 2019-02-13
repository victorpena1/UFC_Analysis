
# High level overview of the project
The main purpose for this project is to understand which combination of martial arts are dominating wins in the UFC.
# Workflow
1. Scrape data from the http://ufcstats.com website.
2. Scrape data from wikipedia. (if time)
3. Data dump into MongoDB.
4. Curate dataset in MongoDB/Pandas/Postgres.
5. Develop a relational database in postgres. (if time)
6. EDA
7. Hypothesis Development.
8. t-test hypothesis.
9. Conclusions

# Data Scrapping
Most of the data is being scraped fro mthe http://ufcstats.com website into 2 main collections:
  1. Events
  2. Fighters
This is data dumped into MongoDB.

# Data dump into MongoDB
As mentioned before, two collections have been created including multiple fields for easy afterwards data manipulation. 

# Data curation process

# Relational Database development
4 tables will be included in this database:
  1. Events info
    * Event Name (name given to the event by the UFC)
    * Date (Date when the event happened)
    * Location (Location where the event happened)
    * Attendance (Number of attendance for each event)
  2. Events fights
  3. Fighters info
  4. Figters Fights 
# EDA
This is going to be mainly statistical understanding of the overall data set. 

# Hypothesis Development
1) 
