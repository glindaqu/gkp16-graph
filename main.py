import pyvis as pv
import networkx as nx


graph = nx.Graph()
points = [("a", "b", 1), ("b", "c", 1), ("a", "c", 1), ("c", "d", 1)]
graph.add_weighted_edges_from(points)

nx.draw(graph, with_labels = True)
nt = pv.network.Network(height='99vh')
nt.from_nx(graph)
nt.show('output/graph.html')

