import numpy as np
import random as rd
import matplotlib.pyplot as plt
from progress.bar import IncrementalBar
from settings import Settings

class World(Settings):
    def __init__(self):
        print("init world")
        super().__init__()
        self.N = self.n_dim
        self.points = [(rd.randint(1, 1000), rd.randint(1, 1000)) for i in range(self.N)]
        self.distanceMatrix = np.zeros((self.N, self.N))
        for i in range(len(self.points)):
            for j in range(len(self.points)):
                self.distanceMatrix[i][j] = self.__calculateDistance(self.points[i], self.points[j])
        self.pheromonesMatrix = np.ones((self.N, self.N))

    def draw(self, bestAgentHistory):
        x, y = zip(*self.points)
        plt.scatter(x, y)
        bar = IncrementalBar('draw', max =len(self.points))
        # Рисуем линии между всеми парами точек
        for i in range(self.N):
            bar.next()
            for j in range(self.N):
                if i != j:
                    plt.plot(
                        [self.points[i][0], self.points[j][0]], 
                        [self.points[i][1], self.points[j][1]], 
                        linewidth=self.pheromonesMatrix[i][j] * 0.1,  # Ширина линии пропорциональна феромонам
                        color='blue',  # Цвет линий
                        alpha=0.5  # Прозрачность линий
                    )
        best = min(bestAgentHistory, key=lambda x: x.wayLen)
        epochBest = bestAgentHistory[-1]
        # self.__drawWay(best.way, color="yellow", linewidth=2.)
        self.__drawWay(best.way, color="red", linewidth=3.)
        
        
        plt.xlim(0, 1000)
        plt.ylim(0, 1000)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.grid()
        plt.show()
        bar.finish()
    
    def __drawWay(self, way: list, **kvargs):
        for k in range(self.N):
            i, j = way[k], way[k+1]
            plt.plot(
                [self.points[i][0], self.points[j][0]], 
                [self.points[i][1], self.points[j][1]], 
                **kvargs
            )
    
    def __calculateDistance(self, point1, point2):
        return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

    def addPheromones(self, i: int, j: int, quantity):
        """
        добавить ферамоны на дорожку между пунктами i и j
        """
        self.pheromonesMatrix[i][j] += quantity
        self.pheromonesMatrix[j][i] += quantity
    
    def evaporation(self, remains: float):
        """
        remains - какая доля ферамонов остается на дорогах (от 0. до 1.)
        """
        self.pheromonesMatrix *= remains


if __name__ == "__main__":
    world = World(22)
    world.draw()