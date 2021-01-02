class Node:
    def __init__(self, value):

        self.value = value


class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacentlist = {}

    def add_vertex(self, node):

        self.adjacentlist[node] = []
        self.number_of_nodes += 1

    def add_edge(self, node1, node2):

        self.adjacentlist[node1] = node2
        self.adjacentlist[node2] = node1

    def show_connections(self):

        allNodes = self.adjacentlist.keys()
        for i in allNodes:
            Nodeconnections = self.adjacentlist[i]
            connections = ""
            vertex = None
            for vertex in Nodeconnections:
                connections += vertex + " "
            print(i, connections)


graph = Graph()
graph.add_vertex("2")
graph.add_vertex("3")
graph.add_edge("2", "3")
graph.add_vertex("33")
graph.show_connections()
print(graph.number_of_nodes)
