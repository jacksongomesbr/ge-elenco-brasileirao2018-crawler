import requests
from bs4 import BeautifulSoup

player_positions = {}
evaluation_criterion = {}
teams = {}

url = 'http://app.globoesporte.globo.com/futebol/brasileirao-serie-a/guia/avaliacao-dos-elencos-brasileirao-2018'
r = requests.get(url)
enc = r.encoding
html = str(r.text.encode(enc), 'utf-8')

bs = BeautifulSoup(html, "lxml")
team_details = bs.select('.team-details-container')
for team_detail in team_details:
    team_id = team_detail.attrs['data-team']
    title = team_detail.select_one('.team-about-title').text
    description = team_detail.select_one('.team-about-description').text
    big_value = team_detail.select_one('.big-value').text
    team_shield_image = team_detail.select_one('.team-shield-image').attrs['src']
    if team_id not in teams:
        teams[team_id] = {
            'name': title,
            'shield_image_url': team_shield_image,
            'description': description,
            'value': big_value,
            'players': {},
            'stats': {}
        }
    for player in team_detail.select('.team-players-list-item'):
        id = player.attrs['data-jogador']
        position_code = player.attrs['data-position']
        criteria_id = player.attrs['data-criteria-id']
        photo = player.select_one('.team-players-list-item-image').attrs['src']
        position_name = player.select_one('.player-position').text
        name = player.select_one('.player-name').text
        criteria_label = player.select_one('.player-evaluation-label').text
        if position_code not in player_positions:
            player_positions[position_code] = position_name
        if criteria_id not in evaluation_criterion:
            evaluation_criterion[criteria_id] = criteria_label
        if criteria_id not in teams[team_id]['stats']:
            teams[team_id]['stats'][criteria_id] = 0
        teams[team_id]['players'][id] = {
            'name': name,
            'photo': photo,
            'position_code': position_code,
            'criteria_id': criteria_id,
        }
        for cid in evaluation_criterion:
            if criteria_id == cid:
                teams[team_id]['stats'][cid] += 1

for id in evaluation_criterion:
    for team in teams:
        if id not in teams[team]['stats']:
            teams[team]['stats'][id] = 0

with open('evaluation_criterion.csv', 'w', encoding='utf-8') as f:
    f.write('"id","label"\n')
    for id, label in evaluation_criterion.items():
        f.write('"{}","{}"\n'.format(id, label))

with open('players_positions.csv', 'w', encoding='utf-8') as f:
    f.write('"id","label"\n')
    for id, label in player_positions.items():
        f.write('"{}","{}"\n'.format(id, label))

with open('teams.csv', 'w', encoding='utf-8') as f:
    headers = ['id', 'name', 'shield_image_url', 'description', 'value']
    for id in evaluation_criterion:
        headers.append('stats_{}'.format(id))
    f.write(','.join(['"{}"'.format(h) for h in headers]) + '\n')
    for team in teams:
        line = [team, teams[team]['name'], teams[team]['shield_image_url'], teams[team]['description'],
                teams[team]['value']]
        for id in evaluation_criterion:
            line.append(teams[team]['stats'][id])
        f.write(','.join(['"{}"'.format(item) for item in line]) + '\n')

with open('players_evaluations.csv', 'w', encoding='utf-8') as f:
    f.write('"team","id","name","photo_url","position","evaluation"\n')
    for team in teams:
        for id, player in teams[team]['players'].items():
            f.write('"{}","{}","{}","{}","{}","{}"\n'.format(team, id, player['name'], player['photo'],
                                                             player['position_code'], player['criteria_id']))
