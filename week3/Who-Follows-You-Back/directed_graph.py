class DirectedGraph:

    def __init__(self):
        self.nodes = {}
        self.visited_nodes = []

    def create_node(self, node):
        if node in self.nodes.keys():
            return False

        self.nodes[node] = []

    def add_edge(self, node_a, node_b):
        if node_a not in self.nodes.keys():
            self.nodes[node_a] = []

        if node_b not in self.nodes.keys():
            self.nodes[node_b] = []

        self.nodes[node_a].append(node_b)

    def get_neighbors_for(self, node):
        if node in self.nodes.keys():
            return self.nodes[node]
        return False

    def path_between(self, node_a, node_b):
        self.visited_nodes.append(node_a)
        if node_b in self.get_neighbors_for(node_a):
            return True
        else:
            for neighbor in self.get_neighbors_for(node_a):
                if neighbor not in self.visited_nodes:
                    if self.path_between(neighbor, node_b):
                        return True
            return False

    def __str__(self):
        output = ""
        for name, follows in self.nodes.items():
            if len(follows) == 0:
                follows = "nobody"

            output += "{} follows {}\n".format(name, follows)

        return output
