import unittest


class TestShortestPath(unittest.TestCase):

    def test_shortest_path(self):
        graph = GraphShortestPath()
        nodes = [graph.add_node(id) for id in range(6)]
        graph.add_edge(0, 1)
        graph.add_edge(0, 4)
        graph.add_edge(0, 5)
        graph.add_edge(1, 3)
        graph.add_edge(1, 4)
        graph.add_edge(2, 1)
        graph.add_edge(3, 2)
        graph.add_edge(3, 4)

        self.assertEqual(graph.shortest_path(nodes[0].key, nodes[2].key), [0, 1, 3, 2])
        self.assertEqual(graph.shortest_path(nodes[0].key, nodes[0].key), [0])
        self.assertEqual(graph.shortest_path(nodes[4].key, nodes[5].key), None)

        print('Success: test_shortest_path')


def main():
    test = TestShortestPath()
    test.test_shortest_path()


if __name__ == '__main__':
    main()
