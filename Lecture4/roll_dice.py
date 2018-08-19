import random
def rollDie():
    return random.choice([1,2,3,4,5,6])
def testroll(n):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print(result)
testroll(5)
