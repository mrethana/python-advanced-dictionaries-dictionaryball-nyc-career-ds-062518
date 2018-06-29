#python -m unittest index_test.py
#learn submit
import pdb


game_dictionary = {'home':{'team_name': 'Brooklyn Nets' , 'colors': ['Black', 'White'], 'players':
{'Alan Anderson': {'number': 0, 'shoe': 16, 'points': 22, 'rebounds': 12, 'assists': 12, 'steals': 3, 'blocks': 1, 'slam_dunks': 1},
'Reggie Evans': {'number': 30, 'shoe': 14, 'points': 12, 'rebounds': 12, 'assists': 12, 'steals': 12, 'blocks': 12, 'slam_dunks': 7},
'Brooke Lopez': {'number': 11, 'shoe': 17, 'points': 17, 'rebounds': 19, 'assists': 10,'steals': 3, 'blocks': 1, 'slam_dunks': 15},
'Mason Plumlee': {'number': 1, 'shoe': 19, 'points': 26, 'rebounds': 12, 'assists': 6, 'steals': 3, 'blocks': 8, 'slam_dunks': 5},
'Jason Terry': {'number': 31, 'shoe': 15, 'points': 19, 'rebounds': 2, 'assists': 2, 'steals': 4, 'blocks': 11, 'slam_dunks': 1}}},
'away':{'team_name': 'Charlotte Hornets', 'colors': ['Turquoise', 'Purple'], 'players':
{'Jeff Adrien': {'number': 4, 'shoe': 18, 'points': 10, 'rebounds': 1, 'assists': 1, 'steals': 2, 'blocks': 7, 'slam_dunks': 2},
'Bismak Biyombo': {'number': 0, 'shoe': 16, 'points': 12, 'rebounds': 4, 'assists': 7, 'steals': 7, 'blocks': 15, 'slam_dunks': 10},
'DeSagna Diop': {'number': 2, 'shoe': 14, 'points': 24, 'rebounds': 12, 'assists': 12, 'steals': 4, 'blocks': 5, 'slam_dunks': 5},
'Ben Gordon': {'number': 8, 'shoe': 15, 'points': 33, 'rebounds': 3, 'assists': 2, 'steals': 1, 'blocks': 1, 'slam_dunks': 0},
'Brendan Haywood': {'number': 33, 'shoe': 15, 'points': 6, 'rebounds': 12, 'assists': 12, 'steals': 22, 'blocks': 5, 'slam_dunks': 12}}}}

def game_dict():
    return game_dictionary

# def home_team_name():
#   return game_dict()['home']['team_name']
# print(home_team_name())
#
# def good_practices():
#     for location, team_stats in game_dict().items():
#         import pdb; pdb.set_trace()
#         for stats, data in team_stats.items():
#             import pdb; pdb.set_trace()
#             for item in data:
#                 print(item)


def num_points_scored(player_name):
    teams = [v['players'] for k, v in game_dictionary.items()]
    players = {}
    for team in teams:
        players.update(team)
        return players[player_name]['points']
#player_points('Alan Anderson')

def shoe_size(player_name):
    teams = [v['players'] for k, v in game_dictionary.items()]
    players = {}
    for team in teams:
        players.update(team)
        return players[player_name]['shoe']
#shoe_size('Alan Anderson')

def team_colors(team_name):
    colors = [v['colors'] for k, v in game_dictionary.items() if v['team_name'] == team_name][0]
    return colors
#team_colors('Brooklyn Nets')

def team_names():
    teams_list = [v['team_name'] for k, v in game_dictionary.items()]
    return teams_list
#team_names()

def player_numbers(team_name):
    for location, team_stat in game_dictionary.items():
        if team_stat['team_name'] == team_name:
            return [team_stat['players'][player]['number'] for player in team_stat['players'].keys()]

#player_numbers('Brooklyn Nets')

def player_stats(player_name):
    teams = [v['players'] for k, v in game_dictionary.items()]
    players = {}
    for team in teams:
        players.update(team)
        return players[player_name]
#player_stats('Alan Anderson')
teams = [v['players'] for k, v in game_dictionary.items()]
players = {}
for team in teams:
    players.update(team)


def big_shoe_rebound():
        shoes = {k:v['shoe'] for k, v in players.items()}
        biggest_shoe = max(shoes.values())
        big_shoe_rebound = [v['rebounds'] for k,v in players.items() if v['shoe'] == biggest_shoe][0]
        return big_shoe_rebound

def most_points():
    points = {k:v['points'] for k, v in players.items()}
    most_points = max(points.values())
    player_most_points = [k for k, v in points.items() if v == max(points.values())][0]
    return player_most_points

def longest_name():
    names = {k:len(k) for k, v in players.items()}
    longest_name = [k for k,v in names.items() if v == max(names.values())]
    return longest_name

def long_name_steals_a_ton():
    longest_name()
    steals = {k:v['steals'] for k, v in players.items()}
    most_steals = max(steals.values())
    player_most_steals = [k for k, v in steals.items() if v == max(steals.values())][0]
    return player_most_steals == longest_name()
