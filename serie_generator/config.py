API_KEY = 'API_KEY' #api.football-data.org
BASE_URL = 'http://api.football-data.org'
HEADERS = {'X-Auth-Token': API_KEY}


ENDPOINTS = {
    'competition': BASE_URL + '/v1/competitions/',
    'competition_teams': BASE_URL + '/v1/competitions/{}/teams',
    'team': BASE_URL + '/v1/teams/{}',
    'team_fixture' : BASE_URL + '/v1/teams/{}/fixtures/'
}

DB = {
  'url': 'MONGO_URL',

}
