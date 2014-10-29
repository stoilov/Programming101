import unittest
from directed_graph import DirectedGraph


class TestDirectedGraph(unittest.TestCase):

    def setUp(self):
        self.graph = DirectedGraph()

    def test_dict_init(self):
        self.assertDictEqual(self.graph.nodes, {})

    def test_create_node(self):
        node = "Ivan"
        self.graph.create_node(node)
        is_created_name = "Ivan" in self.graph.nodes.keys()
        self.assertListEqual(self.graph.nodes["Ivan"], [])
        self.assertTrue(is_created_name)

    def test_create_node_already_created(self):
        node = "Ivan"
        self.graph.create_node(node)
        already_created = self.graph.create_node(node)
        self.assertFalse(already_created)

    def test_add_edge(self):
        node_a = "Ivan"
        self.graph.create_node(node_a)
        node_b = "Gosho"
        self.graph.create_node(node_b)
        self.graph.add_edge(node_a, node_b)
        self.assertDictEqual(self.graph.nodes, {"Ivan": ["Gosho"], "Gosho": []})

    def test_get_neighbours_for(self):
        node_a = "Ivan"
        self.graph.create_node(node_a)
        node_b = "Gosho"
        self.graph.create_node(node_b)
        self.graph.add_edge(node_a, node_b)
        neigbours = self.graph.get_neighbors_for("Ivan")
        self.assertListEqual(neigbours, ["Gosho"])

    def test_get_neighbours_for_no_such_node(self):
        neigbours = self.graph.get_neighbors_for("Stefan")
        self.assertFalse(neigbours)

    def test_path_between(self):
        node_a = "Ivan"
        self.graph.create_node(node_a)
        node_b = "Gosho"
        self.graph.create_node(node_b)
        node_c = "Pesho"
        self.graph.create_node(node_c)
        self.graph.add_edge(node_a, node_b)
        self.graph.add_edge(node_b, node_c)
        is_path = self.graph.path_between(node_a, node_c)
        self.assertTrue(is_path)

    def test_path_between_no_path(self):
        node_a = "Ivan"
        self.graph.create_node(node_a)
        node_b = "Gosho"
        self.graph.create_node(node_b)
        node_c = "Pesho"
        self.graph.create_node(node_c)
        is_path = self.graph.path_between(node_a, node_c)
        self.assertFalse(is_path)

if __name__ == '__main__':
    unittest.main()
