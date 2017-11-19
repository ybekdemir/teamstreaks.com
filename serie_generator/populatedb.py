
import  requests
import  config
from models.competition import Competition
from  models.streak import *
from pymongo import MongoClient


def get_competitions():
    r = requests.get(config.ENDPOINTS.get('competition'), headers=config.HEADERS)
    data = r.json()
    return data

leauges = ['BL1', 'PL', 'SA', 'PD', 'FL1', 'DED', 'PPL']


client = MongoClient(config.DB['url'])
db = client.footballdb

competitions = db.competitions
teams = db.teams
for data in get_competitions():
    if data['league'] in leauges:
        comp  =Competition(data)
        for team in comp.get_teams():
            teams.insert_one(team.__dict__)
        competitions.insert_one(comp.__dict__)



bettypes = db.bettypes
streaktypes = db.streaktypes
id = bettypes.insert_one({'name': '3-Way Result (FT)', 'uid': 1}).inserted_id
streaktypes.insert_one({'name':'Win','uid': 1, 'bet_type_id' : 1})
streaktypes.insert_one({'name':'Draw','uid': 2, 'bet_type_id' : 1})
streaktypes.insert_one({'name':'Lost','uid': 3, 'bet_type_id' : 1})
id = bettypes.insert_one({'name': '3-Way Result (HT)', 'uid': 2}).inserted_id
streaktypes.insert_one({'name':'Win','uid': 4, 'bet_type_id' : 2})
streaktypes.insert_one({'name':'Draw','uid': 5, 'bet_type_id' : 2})
streaktypes.insert_one({'name':'Lost','uid': 6, 'bet_type_id' : 2})
id = bettypes.insert_one({'name': 'Double Chance(FT)','uid': 3}).inserted_id
streaktypes.insert_one({'name':'Undefeated','uid': 7,  'bet_type_id' : 3})
streaktypes.insert_one({'name':'Winless','uid': 8,  'bet_type_id' : 3})
id = bettypes.insert_one({'name': 'Under-Over 1,5 ','uid': 4}).inserted_id
streaktypes.insert_one({'name':'Over','uid': 9,  'bet_type_id' : 4})
streaktypes.insert_one({'name':'Under', 'uid': 10, 'bet_type_id' : 4})
id = bettypes.insert_one({'name': 'Under-Over 3,5 ','uid': 5}).inserted_id
streaktypes.insert_one({'name':'Over','uid': 11,  'bet_type_id' : 5})
streaktypes.insert_one({'name':'Under', 'uid': 12, 'bet_type_id' : 5})
id = bettypes.insert_one({'name': 'Both Team Score','uid': 6}).inserted_id
streaktypes.insert_one({'name':'Yes', 'uid': 13, 'bet_type_id' : 6})
streaktypes.insert_one({'name':'No', 'uid': 14, 'bet_type_id' : 6})




