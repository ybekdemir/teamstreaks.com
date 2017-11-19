

class Match:

    def __init__(self,data):
         self.date = data['date']
         self.status = data['status']
         self.match_day =data['matchday']
         self.home_team_name = data['homeTeamName']
         self.away_team_name = data['awayTeamName']
         self.competition_id = data['_links']['competition']['href'].split('/')[-1]
         self.home_team_score = data['result']['goalsHomeTeam']
         self.away_team_score = data['result']['goalsAwayTeam']
         if 'halfTime' in data['result'].keys():
              self.home_team_ht_score = data['result']['halfTime']['goalsHomeTeam']
              self.away_team_ht_score = data['result']['halfTime']['goalsAwayTeam']




