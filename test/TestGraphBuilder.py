import sys
sys.path.insert(0,"..")

import unittest
from graph.GraphBuilder import GraphBuilder


class TestGraphBuilder(unittest.TestCase):
    def setUp(self):
        self.builder = GraphBuilder()

    def test_build(self):
        self.assertEqual(self.builder.build(), 1)
