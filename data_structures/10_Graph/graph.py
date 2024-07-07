class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph Dict:", self.graph_dict)

    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path

if __name__ == '__main__':

    routes = [
        ("Mumbai","Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune","Hyderabad"),
        ("Pune","Mysuru"),
        ("Hyderabad","Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]

    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_graph = Graph(routes)

    start = "Mumbai"
    end = "New York"

    print(f"All paths between: {start} and {end}: ",route_graph.get_paths(start,end))
    print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start,end))

    start = "Dubai"
    end = "New York"

    print(f"All paths between: {start} and {end}: ",route_graph.get_paths(start,end))
    print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start,end))






#Adjacent list graph representations
#An array contains all vertices and  are connected to a linked list with  the vertices edges(undirected graph)
#in directed graph vertices points to  a linked list with edges i,w where i is index the vertex goes to and w is weight of that edge 

#Adjacent matrix representations
vertexData = ['A','B','C','D']

Adjacency_matrix = [
    [0, 1, 1, 1],  # Edges for A
    [1, 0, 1, 0],  # Edges for B
    [1, 1, 0, 0],  # Edges for C
    [1, 0, 0, 0]   # Edges for D
]
def print_connections(matrix,vertices):
    for i in range(len(vertices)):
        print(f'{vertices[i]}: ',end='')
        for j in range(len(vertices)):
            if matrix[i][j]:
                print(vertices[j], end='')
        print()        

class Graph:
    def __init__(self,size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self,u,v):
        if 0<= u < self.size and  0<= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[u][v] = 1

    def vertex_data(self,vertex,data):
        if 0<= vertex < self.size:
            self.vertex_data[vertex] =  data       
    def print_graph(self):
        for row in self.adj_matrix:
            print(' '.join(map(str,row)))
        for vertex,data in enumerate(self.vertex_data):
            print(f'{vertex} : {data}')    