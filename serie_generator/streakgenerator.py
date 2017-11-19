
import  requests
import  config
import  json
from models.competition import Competition
from models.streak import  *
from models.streakcontroller import  StreakController
import time
from  models.team import  Team
from pymongo import MongoClient


client = MongoClient(config.DB['url'])
db = client.footballdb
teams = db.teams
series = db.series
bettypes = db.bettypes
streaktypes = db.streaktypes


def get_teams():
    team_list = []
    for tm in teams.find():
        team_list.append(Team(tm))
    return team_list

def get_bet_types():
    bet_type_list = []
    for bt in bettypes.find():
        bet_type_list.append(BetType(bt))
    return bet_type_list

def get_streak_types():
    streak_type_list = []
    for st in streaktypes.find():
        streak_type_list.append(StreakType(st))
    return streak_type_list

team_list =get_teams()
bettype_list = get_bet_types()
streak_type_list = get_streak_types()

count = 0

for team in team_list:
    try:
        print(team.name )

        team_match_list = [item for item in team.get_fixture() if item.status == 'FINISHED' and int(item.competition_id) == team.competition_id]

        sorted_matches = sorted(team_match_list, key=lambda x: x.date, reverse=True)

        streak_controller = StreakController(sorted_matches, team)
        streak_controller.control_streaks()
    except:
        continue

    count +=1
    if count == 50:
        time.sleep(10)
        count = 0








