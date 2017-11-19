
import requests
import  config
from .team import  Team

class Competition:


    def __init__(self, data):

        self.teams_url = data['_links']['teams']['href']
        self.id = data['id']
        self.caption = data['caption']
        self.league = data['league']
        self.year = data['year']
        self.number_of_teams = data['numberOfTeams']
        self.number_of_games = data['numberOfGames']
        self.last_updated = data['lastUpdated']

    def get_teams(self):
        r = requests.get(self.teams_url, headers = config.HEADERS)
        data = r.json()
        team_list = []
        for team in data['teams']:
            team['competition_id'] = self.id
            team_list.append(Team(team))
        return  team_list