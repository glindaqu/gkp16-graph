import unittest
from graph.GraphBuilder import GraphBuilder


class TestGraphBuilder(unittest.TestCase):
    def setUp(self):
        self.builder = GraphBuilder()

    def test_build(self):
        self.assertEqual(self.builder.build(), 1)
