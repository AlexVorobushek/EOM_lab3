import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def DrawGraph(nodes, edges):
  G = nx.Graph()
  G.add_nodes_from(nodes)
  G.add_edges_from(edges)
  positions = nx.spring_layout(G)
  distance_dict = dict(nx.all_pairs_dijkstra_path_length(G))
  distance_array_dijkstra = np.array([[distance_dict[i][j] if j in distance_dict[i] else float('inf') for j in G.nodes()] for i in G.nodes()])
  result = nx.draw(G, positions, with_labels=True)
  plt.show()
  return distance_array_dijkstra
print(DrawGraph([1, 2, 3, 4], [(1, 2), (1, 3), (2, 3), (3, 4)]))