from World import World
from Agent import Agent
from time import time
from settings import Settings
from progress.bar import IncrementalBar

class AntAlgo(Settings):
    def __init__(self):
        super().__init__()
        self.bestAgentHistory: list[Agent] = []
        self.world = World()
    
    def runIteration(self):
        self.world.evaporation(self.remainsPheromone)
        newAgents: list[Agent] = [Agent(self.world).run() for _ in range(self.pop_size)]
        self.bestAgentHistory.append(min(newAgents, key=lambda agent: agent.wayLen))
        bar = IncrementalBar('run', max=self.pop_size)
        for agent in newAgents:
            agent.sprayPheromone()
            bar.next()
        bar.finish()

    def run(self):
        timeStart = time()
        epoch = 1
        while time() < timeStart + 900:
            self.runIteration()
            print(f"{epoch=}")
            
            if not epoch%10:
                best = min(self.bestAgentHistory, key=lambda x: x.wayLen)
                epochBest = self.bestAgentHistory[-1]
                print("best:", best.wayLen)
                print("epoch best:", epochBest.wayLen)
                algo.world.draw(algo.bestAgentHistory)
            
            epoch += 1
            


if __name__=="__main__":
    algo = AntAlgo()
    algo.run()
