import unittest
from TestGraphBuilder import TestGraphBuilder


def graph_builder_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestGraphBuilder('test_build'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(graph_builder_suite())