import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), '../graph_builder', 'graph'))

import unittest
from graph.GraphBuilder import GraphBuilder


class TestGraphBuilder(unittest.TestCase):
    def setUp(self):
        self.builder = GraphBuilder()

    def test_build(self):
        self.assertEqual(self.builder.build(), 1)
