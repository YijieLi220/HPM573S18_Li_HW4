import random

class Game:
    def __init__(self,id):
        self.id =id
    def simulation(self):
        x =-250
        i = 0
        j=0
        step=["H","T","H","T","H","T","H","T","H","T","H","T","H","T","H","T","H","T","H","T"] #create the list called step.
        for j in range(0,len(step)):
           step[j]=random.choice(["H","T","H","T","H","T","H","T","T","T"])  #setting the prob, where p(H)=0.4
           j=j+1
        for i in range(0,18):
            if step[i] == 'T' and step[i+1]=='T' and step[i+2]=='H':
                x +=100
                i=i+3
            else:
                x +=0
                i=i+1
        return x

class Cohort:
    def __init__(self,id,pop_size):

        self.step=[]
        self.total_score=[]
        n=1
        while n<=pop_size:
            gameunit=Game(id*pop_size+n)
            self.step.append(gameunit)
            n+=1

    def simulatecohort(self):
        for game in self.step:
            value=game.simulation()
            self.total_score.append(value)

    def get_expected_score(self):
        return sum(self.total_score)/len(self.total_score)

test = Cohort(1, 1000)
test.simulatecohort()
print("The expected score is", test.get_expected_score())