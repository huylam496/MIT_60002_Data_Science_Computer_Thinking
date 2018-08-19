import random
def rollDie():
    return random.choice([1,2,3,4,5,6])

def runSim(goal, numTrials, txt):
    total = 0
    for i in range(numTrials):
        result = ''
        for j in range(len(goal)):
            #print('result before = ', result)
            result += str(rollDie())
            #print('result after = ', result)
        if result == goal:
            total += 1
    print('Approximated probability of', txt, '=', round(total/numTrials,8))
    print('Accurate probability of', txt, '=', round(1/(6**len(goal)),8))

runSim('111111', 10000, '111111')


