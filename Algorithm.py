import ast
from collections import deque, namedtuple


both_ends = True
nodoinit=""
nodofin=""


inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')

Grafo= []
#read txt
archivo=open('nodos.txt','r')
for lista in archivo.readlines():
    nt= lista.replace("\n", "")
    nt2= ast.literal_eval(nt)
    Grafo.append(nt2)
archivo.close()

#menu
def menu():
    print("El grafo a evaluar es... ¿dirgido (1) o no dirgigido (0)?")
    choice = input()
    if choice == "1":
        both_endsl=False
        both_ends=both_endsl 
        print("El grafo es Dirigido")
        print("Elija el nodo de inicio")
        nodoinit = input()   
        print("Elija el nodo final")
        nodofin = input()
        print("La ruta más corta es : ")
        # print(str(both_ends))
        # print(str(nodoinit))
        # print(str(nodofin))
        print(graph.dijkstra(str(nodoinit), str(nodofin)))
    elif choice == "0":
        both_endsl=True
        both_ends=both_endsl
        print("El grafo es No dirigido")
        print("Elija el nodo de inicio")
        nodoinit = input()   
        print("Elija el nodo final")
        nodofin = input()
        print("La ruta más corta es : ")
        # print(str(both_ends))
        # print(str(nodoinit))
        # print(str(nodofin))
        print(graph.dijkstra(str(nodoinit), str(nodofin)))
    else:
        print("Inserte una opción válida\n")
        menu()
    return both_ends

def eleccion():
    print("Elija el nodo de inicio")
    nodoinit = input()
    
    print("Elija el nodo final")
    nodofin = input()
    

#Program
def make_edge(start, end, cost=1):
    return Edge(start, end, cost)


class Graph:
    def __init__(self, edges):
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]   

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )

    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Such source node doesn\'t exist'
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        return path


# for i in variable:
#     print(type(i))

#graph = nods
graph = Graph(Grafo)

menu()
