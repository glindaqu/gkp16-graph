import unittest
from TestGraphBuilder import TestGraphBuilder
from TestYamlParser import TestYamlParser


def graph_builder_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestGraphBuilder("test_build_1"))
    suite.addTest(TestGraphBuilder("test_build_2"))
    suite.addTest(TestGraphBuilder("test_build_3"))
    suite.addTest(TestGraphBuilder("test_build_4"))
    return suite


def yaml_parser_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestYamlParser("test_parse_1"))
    suite.addTest(TestYamlParser("test_parse_2"))
    suite.addTest(TestYamlParser("test_parse_3"))
    suite.addTest(TestYamlParser("test_parse_4"))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(graph_builder_suite())
    runner.run(yaml_parser_suite())
