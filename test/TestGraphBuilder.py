import unittest
from graph.GraphBuilder import GraphBuilder
from graph.GraphBuilderReturnCode import GraphBuilderReturnCode
import os


class TestGraphBuilder(unittest.TestCase):
    def setUp(self):
        self.builder = GraphBuilder()

    # if both of files are falsy
    def test_build_1(self):
        self.assertEqual(
            self.builder.build("", ""),
            GraphBuilderReturnCode.FILE_DOES_NOT_EXISTS,
        )

    # if yaml file are falsy
    def test_build_2(self):
        self.assertEqual(
            self.builder.build(
                "", os.path.dirname(os.path.abspath(__file__)) + "../output/file.html"
            ),
            GraphBuilderReturnCode.FILE_DOES_NOT_EXISTS,
        )

    # if output filepath empty
    def test_build_3(self):
        self.assertEqual(
            self.builder.build(
                os.path.dirname(os.path.abspath(__file__)) + "/../data/struct.yaml", ""
            ),
            GraphBuilderReturnCode.OUTPUT_FILE_PATH_EMPTY,
        )

    # common situation
    def test_build_4(self):
        self.assertEqual(
            self.builder.build(
                os.path.dirname(os.path.abspath(__file__)) + "/../data/struct.yaml",
                "graph.html",
            ),
            GraphBuilderReturnCode.OK,
        )
