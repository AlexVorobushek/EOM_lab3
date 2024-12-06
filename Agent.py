from World import World
from random import randint, random
from settings import Settings

class Agent(Settings):
    def __init__(self, world: World):
        super().__init__()
        self.world = world
        self.way = None
        self.wayLen = None
        self.providedPheromones = 0
    
    def run(self, startPoint: int = None):
        nowPoint = startPoint if startPoint else randint(0, self.world.N-1)
        resultWay = [nowPoint]
        resultLen = 0
        notVisited = set(range(self.world.N)) - {nowPoint}
        while notVisited:
            nextPoint = self.__chooseNextPoint(nowPoint, notVisited)
            resultWay.append(nextPoint)
            resultLen += self.world.distanceMatrix[nowPoint][nextPoint]
            notVisited -= {nextPoint}
            nowPoint = nextPoint
        resultWay.append(resultWay[0])
        resultLen += self.world.distanceMatrix[nowPoint][resultWay[0]]
        self.way = resultWay
        self.wayLen = resultLen
        return self
    
    def __chooseNextPoint(self, nowPoint, notVisited: set) -> int:
        notVisitedLen = len(notVisited)
        if notVisitedLen == 1: return list(notVisited)[0]
        notVisited = list(notVisited)
        hopes = [
            self.world.pheromonesMatrix[nowPoint][j]**self.alpha +
            (self.world.distanceMatrix[nowPoint][j]/1000)**(-self.beta)
            for j in notVisited
        ]
        sumHope = sum(hopes)
        for i in range(notVisitedLen):
            hopes[i] /= sumHope
        # return notVisited[notVisitedRoulette.index(max(notVisitedRoulette))]
        scroll = random()
        resInd = 0
        integrator = 0.
        
        # hopes[-1] -= sumHope-1
        # for i in range(len(notVisited)):
        #     pointInd = notVisited[i]
        #     print(i, round(self.world.pheromonesMatrix[nowPoint][pointInd], 3), round(self.world.distanceMatrix[nowPoint][pointInd], 3), round(notVisitedRoulette[i], 3))
        # print("--------------")
        while scroll > integrator+hopes[resInd]:
            integrator += hopes[resInd]
            resInd+=1

        return notVisited[resInd]
    
    def sprayPheromone(self):
        for i in range(self.world.N - 1):
            self.world.addPheromones(self.way[i], self.way[i+1],  self.Q/self.wayLen)
    
