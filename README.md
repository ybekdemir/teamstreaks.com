
# TEAMSTREAKS

Code behind the teamstreaks.com (For demonstration in Scisports interview).

 TeamStreaks follows matches on active tournaments, turns results into form series and serves final statistics with user friendly table.
 It's simple but very useful data for betting players. Because, most players focus on well-known team for their bets, but sometimes the team from 
 unpopular league may be more dominant than Real Madrid in their league.

I used python and Node.js(Express.js for backend and React.js for frontend). 

**Note**:  I should state that I developed this application in one day and I didn't write comment and test.

The project consist of 3 main part.

#### Streak Generator
 
Streak Generator written in python. It's fetching match result from **api.football-data.org** and calculating series for each team
 and writing results on MongoDB database. It's commandline application.
 
#### API

API is written by using Express.js. It's fetching data from database and formatting this data to JSON to serve client application.
API is running on Heroku container engine. 
    
You can access API on https://damp-meadow-47784.herokuapp.com/api/. 
    

Example usages:    
```

https://damp-meadow-47784.herokuapp.com/api/data/tournaments (Get all tournaments)
https://damp-meadow-47784.herokuapp.com/api/team/all    (Get all teams)
https://damp-meadow-47784.herokuapp.com/api/team/5a11c4727439e45bc792999b ( Get team by id)
https://damp-meadow-47784.herokuapp.com/api/streak      (all streaks)
https://damp-meadow-47784.herokuapp.com/api/streak/1    (by streak_id)
https://damp-meadow-47784.herokuapp.com/api/streak/1/445 (by streak_id/tournament)
https://damp-meadow-47784.herokuapp.com/api/data/bettypes (get bet types)
```

#### Client

For client application, I used **React.js** and **bulma**(https://bulma.io/). Client application fetching data from API and turning this data to
simple table. 


  
