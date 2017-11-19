


class BetType:

    def __init__(self, data):
        self.name = data['name']
        self.id = data['_id']

class StreakType:

    def __init__(self, data):
        self.name = data['name']
        self.id = data['_id']
        self.bet_type_id = data['bet_type_id']

class Streak:

    def __init__(self, data):
        self.id = data['id']
        self.team_id = data['id']
        self.competition_id = data['competition_id']
        self.count = data['count']
        self.streak_type_id = ['streak_type_id']




