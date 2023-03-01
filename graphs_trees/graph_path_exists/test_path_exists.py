import unittest


class TestPathExists(unittest.TestCase):

    def test_path_exists(self):
        graph = GraphPathExists()
        nodes = [graph.add_node(id) for id in range(6)]
        graph.add_edge(0, 1, 5)
        graph.add_edge(0, 4, 3)
        graph.add_edge(0, 5, 2)
        graph.add_edge(1, 3, 5)
        graph.add_edge(1, 4, 4)
        graph.add_edge(2, 1, 6)
        graph.add_edge(3, 2, 7)
        graph.add_edge(3, 4, 8)

        self.assertEqual(graph.path_exists(nodes[0], nodes[2]), True)
        self.assertEqual(graph.path_exists(nodes[0], nodes[0]), True)
        self.assertEqual(graph.path_exists(nodes[4], nodes[5]), False)

        print('Success: test_path_exists')


def main():
    test = TestPathExists()
    test.test_path_exists()


if __name__ == '__main__':
    main()
