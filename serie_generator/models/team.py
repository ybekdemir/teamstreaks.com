import config
import requests
from pymongo import MongoClient
from models.match import  Match

class Team:

    def __init__(self, data):
        if '_id' in data.keys():
            self.id =  data['_id']

        self.name = data['name']
        self.code = data['code']
        if 'shortName' in data.keys():
            self.short_name = data['shortName']
        else:
            self.short_name = data['short_name']

        self.squadMarketValue = data['squadMarketValue']

        if 'crestUrl' in data.keys():
            self.crest_url = data['crestUrl']
        else:
            self.crest_url = data['crest_url']
        if '_links' in data.keys():
            self.fixture_url = data['_links']['fixtures']['href']
        else:
            self.fixture_url = data['fixture_url']

        self.competition_id = data['competition_id']

    def get_fixture(self):

        r = requests.get(self.fixture_url, headers = config.HEADERS)
        data = r.json()
        match_list = []
        for item in data['fixtures']:
            match_list.append(Match(item))
        return  match_list

