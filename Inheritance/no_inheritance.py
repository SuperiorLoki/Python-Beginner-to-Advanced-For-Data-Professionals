'''
Classes are useful because it is better for readability and better structure
Just like Java, you have objects and you have attributes for it and methods
'''
import datetime


class TennisPlayer:
    def __init__(self, fname, lname, birth_year):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = birth_year
        self.aces = []

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year

    def get_average_aces_per_match(self):
        return sum(self.aces) / len(self.aces)

    def add_ace(self, num_aces):
        self.aces.append(num_aces)


class CricketPlayer:
    team_size = 11

    def __init__(self, fname, lname, birth_year, tname):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = birth_year
        self.team_name = tname
        self.scores = []

    # These are the methods of the class
    def add_score(self, score):
        self.scores.append(score)

    def get_average_score(self):
        return sum(self.scores) / len(self.scores)

    # It's like a toString() method and it highlights the instance of the class
    def __str__(self):
        return f"{self.first_name} {self.last_name}, born in the year {self.birth_year}, plays for {self.team_name}"

    # Operator Overloading
    # You can use this if you have to compare two objects for something
    # lt stands for less than so the return has to make sure the self is less than the other one. There is also __eq__ and __gt__
    def __lt__(self, other):
        self_avg_score = self.get_average_score()
        other_avg_score = other.get_average_score()
        return self_avg_score < other_avg_score


# Instance of the class
virat = CricketPlayer('virat', 'kohli', 1988, "Royal Challengers Bangalore")
print(virat.first_name)
print(virat.last_name)
print(virat.birth_year)
print(virat.team_name)
virat.add_score(75)
virat.add_score(82)
virat.add_score(65)
print(virat.get_average_score())
print(virat)

roger = TennisPlayer('Roger', 'Federer', 1980)
print(roger.get_age())