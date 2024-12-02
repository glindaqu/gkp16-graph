import unittest
from TestGraphBuilder import TestGraphBuilder


def graph_builder_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestGraphBuilder("test_build_1"))
    suite.addTest(TestGraphBuilder("test_build_2"))
    suite.addTest(TestGraphBuilder("test_build_3"))
    suite.addTest(TestGraphBuilder("test_build_4"))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(graph_builder_suite())
