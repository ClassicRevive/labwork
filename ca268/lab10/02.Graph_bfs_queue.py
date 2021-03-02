""" A Python Class
A simple Python graph class, demonstrating the essential 
facts and functionalities of graphs.
"""
from collections import deque

class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def bfs(self, v, visited):
        if v in visited:
            return

        visited.append(v)
        graph = self.__graph_dict

        queue = deque(v)
        while not len(queue) == 0:
            v = queue.popleft()
            if not v in visited:
                visited.append(v)
            for vertex in graph[v]:
                if not vertex in visited:
                    queue.append(vertex)

    def dfs(self, v, visited):
        if v in visited:
            return

        visited.append(v)
        graph = self.__graph_dict

        stack = [v]
        while not len(stack) == 0:
            v = stack.pop()
            if not v in visited:
                visited.append(v)
            for vertex in graph[v]:
                if not vertex in visited:
                    stack.append(vertex)
                    break


    def rec_dfs(self, v, visited):
        if v in visited:
            return

        visited.append(v)
        graph = self.__graph_dict

        for vertex in graph[v]:
            print("dfs", visited)
            if not vertex in visited:
                self.rec_dfs(vertex, visited)


    @staticmethod
    def dijkstra(graph, start):
        # distance between start node and each node on the graph
        graph = graph.__graph_dict
        inf = 999999
        dists = []
        for node in graph:
            for edge in node:
                dists.append(inf)

        print(dists)
        

if __name__ == "__main__":
    # test script for graph
    g = { "a" : ["b", "c", "f", ],
          "b" : ["a", "c", "d", ],
          "c" : ["a", "b", "d", "f"],
          "d" : ["b", "c", "e",],
          "e" : ["d", "f"],
          "f" : ["a", "c", "e",]
        }

    graph = Graph(g)

    visited = []

    graph.bfs("a", visited)
    print("bfs:")
    print(visited)
    visited = []
    
    graph.rec_dfs("a", visited)
    print("recursive dfs:")
    print(visited)
    visited = []
    graph.dfs("a", visited)
    print("stack dfs:")
    print(visited)


