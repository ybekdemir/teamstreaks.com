import  requests
import  config
from models.competition import Competition
from  models.team import  Team
from models.streak import  Streak
from pymongo import MongoClient


class StreakController:

    def __init__(self, data, team):
        self.fixture_data = data
        self.team = team

    def control_streaks(self):
        self.control_ft_win_streak()
        self.control_ft_draw_streak()
        self.control_ft_lost_streak()
        self.control_ft_both_team_score_streak()
        self.control_ft_either_team_not_score_streak()
        self.control_ft_winless_streak()
        self.control_ft_undefeated_streak()
        self.control_ft_over_1_5_streak()
        self.control_ft_under_1_5_streak()
        self.control_ft_over_3_5_streak()
        self.control_ft_under_3_5_streak()


    def generate_streak(self, competition_id, team_id, count, streak_type_id):
        client = MongoClient(config.DB['url'])
        db = client.footballdb
        straks_collection =db.streaks
        id = straks_collection.insert_one(
                                    {'team_id':team_id, 'competition_id':competition_id,
                                     'count':count, 'streak_type_id': streak_type_id, 'team_name':self.team.name}).inserted_id

        return id

    def control_ft_win_streak(self):
        count = 0
        for match in self.fixture_data:
            if  match.status == 'FINISHED':
                if match.home_team_name == self.team.name and match.home_team_score > match.away_team_score:
                    count += 1
                elif match.away_team_name == self.team.name and match.home_team_score < match.away_team_score:
                     count += 1
                else:
                    break

        if count >2:
            self.generate_streak(self.team.competition_id, self.team.id, count, 1)


    def control_ft_draw_streak(self):
        count = 0
        for match in self.fixture_data:
            if match.status == 'FINISHED':
                if match.home_team_score == match.away_team_score:
                    count += 1
                else:
                    break

        if count >2:
            self.generate_streak(self.team.competition_id, self.team.id, count, 2)


    def control_ft_lost_streak(self):
        count = 0
        for match in self.fixture_data:
            if match.status == 'FINISHED':
                if match.home_team_name == self.team.name and match.home_team_score < match.away_team_score:
                    count += 1
                elif match.away_team_name == self.team.name and match.home_team_score > match.away_team_score:
                     count += 1
                else:
                    break

        if count >2:
            self.generate_streak(self.team.competition_id, self.team.id, count, 3)

    def control_ft_win_streak(self):
        count = 0
        for match in self.fixture_data:
            if  match.status == 'FINISHED':
                if match.home_team_name == self.team.name and match.home_team_ht_score > match.away_team_ht_score:
                    count += 1
                elif match.away_team_name == self.team.name and match.home_team_ht_score < match.away_team_ht_score:
                     count += 1
                else:
                    break

        if count >2:
            self.generate_streak(self.team.competition_id, self.team.id, count, 4)


    def control_ft_draw_streak(self):
        count = 0
        for match in self.fixture_data:
            if match.status == 'FINISHED':
                if match.home_team_ht_score == match.away_team_ht_score:
                    count += 1
                else:
                    break

        if count >2:
            self.generate_streak(self.team.competition_id, self.team.id, count, 5)


    def control_ft_lost_streak(self):
        count = 0
        for match in self.fixture_data:
            if match.status == 'FINISHED':
                if match.home_team_name == self.team.name and match.home_team_ht_score < match.away_team_ht_score:
                    count += 1
                elif match.away_team_name == self.team.name and match.home_team_ht_score > match.away_team_ht_score:
                     count += 1
                else:
                    break

        if count >2:
            self.generate_streak(self.team.competition_id, self.team.id, count, 6)


    def control_ft_undefeated_streak(self):
        count = 0
        for match in self.fixture_data:
            if match.status == 'FINISHED':
                if match.home_team_name == self.team.name and match.home_team_score >= match.away_team_score:
                    count += 1
                elif match.away_team_name == self.team.name and match.home_team_score <= match.away_team_score:
                     count += 1
                else:
                    break

        if count >2:
            self.generate_streak(self.team.competition_id, self.team.id, count, 7)


    def control_ft_winless_streak(self):
        count = 0
        for match in self.fixture_data:
            if match.status == 'FINISHED':
                if match.home_team_name == self.team.name and match.home_team_score <= match.away_team_score:
                    count += 1
                elif match.away_team_name == self.team.name and match.home_team_score >= match.away_team_score:
                     count += 1
                else:
                    break

        if count >2:
            self.generate_streak(self.team.competition_id, self.team.id, count, 8)

    def control_ft_over_1_5_streak(self):
        count = 0
        for match in self.fixture_data:
            if match.status == 'FINISHED':
                if match.home_team_score + match.away_team_score > 1.5:
                    count += 1
                else:
                    break

        if count >2:
            self.generate_streak(self.team.competition_id, self.team.id, count, 9)

    def control_ft_under_1_5_streak(self):
        count = 0
        for match in self.fixture_data:
            if match.status == 'FINISHED':
                if match.home_team_score + match.away_team_score < 1.5:
                    count += 1
                else:
                    break

        if count >2:
            self.generate_streak(self.team.competition_id, self.team.id, count, 10)

    def control_ft_over_3_5_streak(self):
        count = 0
        for match in self.fixture_data:
            if match.status == 'FINISHED':
                if match.home_team_score + match.away_team_score > 3.5:
                    count += 1
                else:
                    break

        if count > 2:
            self.generate_streak(self.team.competition_id, self.team.id, count, 11)

    def control_ft_under_3_5_streak(self):
        count = 0
        for match in self.fixture_data:
            if match.status == 'FINISHED':
                if match.home_team_score + match.away_team_score < 3.5:
                    count += 1
                else:
                    break

        if count > 2:
            self.generate_streak(self.team.competition_id, self.team.id, count, 12)

    def control_ft_both_team_score_streak(self):
        count = 0
        for match in self.fixture_data:
            if match.status == 'FINISHED':
                if match.home_team_score>0 and match.away_team_score > 0:
                    count += 1
                else:
                    break

        if count > 2:
            self.generate_streak(self.team.competition_id, self.team.id, count, 13)

    def control_ft_either_team_not_score_streak(self):
        count = 0
        for match in self.fixture_data:
            if match.status == 'FINISHED':
                if match.home_team_score == 0  and match.away_team_score == 0:
                    count += 1
                else:
                    break

        if count > 2:
            self.generate_streak(self.team.competition_id, self.team.id, count, 14)


