import datetime


#We create a parent class for this
class Player:
    def __init__(self, fname, lname, birth_year):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = birth_year

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year


class TennisPlayer(Player):
    def __init__(self, fname, lname, birth_year):
        #Delegates the inputs to the parent class...only the ones we want to delegate
        super().__init__(fname, lname, birth_year)
        self.aces = []

    def get_average_aces_per_match(self):
        return sum(self.aces)/len(self.aces)

class CricketPlayer(Player):
    def __init__(self, fname, lname, team, birth_year):
        #Delegates the inputs to the parent class...only the ones we want to delegate
        super().__init__(fname, lname, birth_year)
        #The team is not delegated to parent class and we set that to the team variable
        self.team = team
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_average_score(self):
        return sum(self.scores) / len(self.scores)

#Despite the TennisPlayer class not having anything in it, this will work
#This is because it takes the information from the parent class as there is nothing in the child class
roger = TennisPlayer("roger", "federer", 1980)
print(roger.first_name)

virat = CricketPlayer("Virat", "Kohli", "RCB", 1988)
virat.add_score(50)
virat.add_score(86)
virat.add_score(99)

#We have the get_age function in the parent class and so that will be common
#Side Note: Having a comma to concatenate will let you add an int
print("Age of Virat Kohli: ", virat.get_age())
print("Age of Roger Federer: ", roger.get_age())

#The average score and average aces will both be different however
print("Virat's average score: " + str(virat.get_average_score()))

