import random, pylab

#Set line width
pylab.rcParams['Lines.linewidth'] = 4
#set font size for tittles
pylab.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
pylab.rcParams['xtick.labelsize'] = 16
#set size of numbers on y-axis
pylab.rcParams['ytick,labelsize'] = 16
#set size of ticks on x-axis
pylab.rcParams['xtick.major.size'] = 7
#set size of ticks on y-axis
pylab.rcParams['ytick.major.size'] = 7
#set size of markers, e.g, circles representing

class Location(object):
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x
    def getY(self):
        return self.y

    def distFrom(self, other):
        xDist = self.x - other.getX()
        yDist = self.y - other.getY()
        return (xDist**2 + yDist**2)**0.5
    
    def __str__(self):
        return '<' + str(self.x) + ','\
                   + str(self.y) + '>'

class Drunk(object):
    def __init__(self, name = None):
        """Assumes name í a str"""
        self.name = name

    def __str__(self):
        if self != None:
            return self.name
        return 'Anonymous'

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0,1), (0,-1), (1,0), (-1,0)]
        return random.choice(stepChoices)

class MasochistDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0, 1.1), (0.0, -0.9), (1.0,0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class Field(object):
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        #use move method of Location to get new location
        self.drunks[drunk]= self.drunks[drunk].move(xDist, yDist)

def walk(f, d, numSteps):
    """Assumes: f a Field, d a Drunk in f, and
        numSteps an int >= 0.
        Moves d numSteps times; returns the distance
        between the final location and the location
        at the start of the walk"""
    start =  f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))

def simWalks(numSteps, numTrials, dClass):
    """Assumes numSteps an int >= 0, numTrials an
        int >0, dClass a subclass of Drunk
        Simulates numTrials walks of numSteps steps
        each. Returns a list of the final distances
        for each trial"""
    Homer = dClass()
    origin = Location(0,0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f, Homer, numTrials),1))
    return distances
def drunkTest(walkLengths, numTrials, dClass):
    """Assumes walkLengths a sequence of ints >=0
        numTrials an int > 0,
        dClass a subclass of Drunk
       For each number of steps in walkLengths,
        runs simWalks with numTrials walks and prints results"""
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__,'random walk of', numSteps, 'steps')
        print(' Mean = ', round(sum(distances)/len(distances),4))
        print(' Max = ', max(distances), 'Min = ', min(distances))

drunkTest((10, 100, 1000, 10000), 100, UsualDrunk)



class styleIterator(object):
    def __init__(self, styles):
        self.index = 0
        self.styles = styles
    def nextStyle(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) -1:
            self.index = 0
        else:
            self.index +=1
            return result

def simDrunk(numTrials, dClass, walkLengths):
    meanDistances = []
    for numSteps in walkLengths:
        print('Starting simulation of', numSteps, 'steps')
        trials = simWalks(numSteps, numTrials, dClass)
        mean = sum(trials)/len(trials)
        mean.Distances.append(mean)
    return meanDistances

def simAll(drunkKinds, walkLengths, numTrials):
    styleChoice = styleIterator(('m-', 'b--', 'g-.'))
    for dClass in drunkKinds:
        curStyle = styleChoice.nextStyle()
        print('Starting simulation of', dClass.__name__)
        means = simDrunk(numTrials, dClass, walkLengths)
        pylab.plot(walkLengths, means, curStyle,
                   label = dClass.__name__)
        pylab.title('Mean Distance from Origin (' 
                    +str(numTrials) + 'trials)')
        pylab.xlabel('Number of Steps')
        pylab.ylabel('Distance from Origin')
        pylab.legend(loc = 'best')
 
random.seed(0)
numSteps = (10,100,1000,10000,100000)
simAll((UsualDrunk, MasochistDrunk), numSteps, 100)

pylab.plot(numSteps, pylab.array(numSteps)**0.5, 'k-.',
           label = 'Square root of steps')
pylab.plot(numSteps, pylab.array(numSteps)*0.05, 'g-.',
           label = 'numSteps*0.05')
pylab.legend(loc = 'best')



        
        
        
        
            
