import random
import math
def sameDate(numPeople, numSame):
    """This function take in the number of people
        and generate a random birthday for each person
        and compare the max # of same date with numSame"""
    possible_day = range(366)
    birthday = [0]*366
    for i in range(numPeople):
        birthdate = random.choice(possible_day)
        birthday[birthdate] +=1
    return max(birthday) >= numSame

def birthdayProb(numPeople, numSame, numTrials):
    """This function find the probability of people have the same
        over total trials"""
    numhits = 0
    for i in range(numTrials):
        if sameDate(numPeople, numSame):
            numhits +=1
    prob = numhits/numTrials
    return prob

for numPeople in [10, 20, 40, 100]:
    print('For', numPeople, 'est.prob. of a shared birthday is', birthdayProb(numPeople, 2, 10000))
    numerator = math.factorial(366)
    denom = (366**numPeople)*math.factorial(366 - numPeople)
    print('Actual prob. for N = 100 =', 1 - numerator/denom)
    
