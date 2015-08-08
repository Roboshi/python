import OSN
from igraph import *

def main ():
        g = Graph()
        
        new_vertex_id = g.vcount()
        g.add_vertices(6)
        g.add_edges([(0,1), (1,2), (2,3), (3,4), (4,5), (5,3)])

        new_vertext_id = g.vcount()
        g2 = Graph.Tree(127, 2)
        g2.get_edgelist() == g.get_edgelist()

        g = Graph([(0,1), (0,2), (2,3), (3,4), (4,2), (2,5), (5,0), (6,3), (5,6)])
        g.vs["name"] = ["Vanessa", "Tumi", "Nwabisa", "Alex", "Karissa", "Saqib", "Alex"]
        g.vs["age"] = [21, 22, 27, 23, 20, 21, 29]
        g.vs["gender"] = ["f", "m", "f", "m", "f", "m", "m"]
        """g.es["is_formal = False, False, True, True, True, False, True, False, False"]"""

        g.degree([2,3,4])

        new_edge_id = g.ecount()
        g.es.edge_betweenness()
        g.vs[2].degree()

        g.vs.select(_degree = g.maxdegree())["name"]
        seq = g.vs.select(None)
        len(seq)

        graph = Graph.Full(10)
        only_odd_vertices = graph.vs.select(lambda vertex: vertex.index % 2 == 1)
        len(only_odd_vertices)
  
        seq = graph.vs.select([2, 3, 7])
        len(seq)

        [v.index for v in seq]

        seq = seq.select([0, 2])
        [v.index for v in seq]

        seq = graph.vs.select([2, 3, 7, "foo", 3.5])
        len(seq)

        layout = g.layout_kamada_kawai()
        layout = g.layout("kamada_kawai")

        g.vs["label"] = g.vs["name"]
        color_dict = {"m": "blue", "f": "pink"}
        g.vs["color"] = [color_dict[gender] for gender in g.vs["gender"]]
       
        plot(g, layout = layout, bbox = (300, 300), margin = 20)

main ()
