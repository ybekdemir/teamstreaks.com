API_KEY = 'd32094bec3174230a381a809ec302290'
BASE_URL = 'http://api.football-data.org'
HEADERS = {'X-Auth-Token': API_KEY}


ENDPOINTS = {
    'competition': BASE_URL + '/v1/competitions/',
    'competition_teams': BASE_URL + '/v1/competitions/{}/teams',
    'team': BASE_URL + '/v1/teams/{}',
    'team_fixture' : BASE_URL + '/v1/teams/{}/fixtures/'
}

DB = {
  'url': 'mongodb://teamstreaksapp:teamstreaks!!@ds259855.mlab.com:59855/footballdb',
}
