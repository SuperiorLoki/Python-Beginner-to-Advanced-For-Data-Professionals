import datetime
def get_avg_score(player):
    return sum(player['scores'])/len(player['scores'])

def get_age(player):
    current_year = datetime.datetime.now().year
    return current_year-player['birth_year']

virat = {
    'first_name': 'virat',
    'last_name': 'kohli',
    'scores':[],
    'birth_year': 1988
}

virat['scores'].append(80)
virat['scores'].append(50)
virat['scores'].append(20)

print(get_avg_score(virat))
print(get_age(virat))

david = {
    'first_name': 'david',
    'last_name': 'warner',
    'scores':[],
    'birth_year': 1986
}

david['scores'].append(180)
david['scores'].append(50)
david['scores'].append(90)

print(get_avg_score(david))
print(get_age(david))