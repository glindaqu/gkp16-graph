from yaml_parser.YamlParser import YamlParser
from graph.GraphBuilderException import GraphBuilderException
from yaml_parser.YamlParserReturnCode import YamlParserReturnCode
from graph.GraphBuilderReturnCode import GraphBuilderReturnCode
import pyvis as pv
import networkx as nx
import os


class GraphBuilder:
    def build(self, yaml: str, html: str) -> int:
        if not os.path.isfile(yaml):
            return GraphBuilderReturnCode.FILE_DOES_NOT_EXISTS
        elif not html:
            return GraphBuilderReturnCode.OUTPUT_FILE_PATH_EMPTY

        self.parser = YamlParser()
        result = self.parser.build(yaml)

        if result == YamlParserReturnCode.PERMISSION_DENIED:
            return GraphBuilderReturnCode.PERMISSION_DENIED
        elif result == YamlParserReturnCode.FILE_DOES_NOT_EXISTS:
            return GraphBuilderReturnCode.FILE_DOES_NOT_EXISTS

        contents = self.parser.get_contents()

        graph = nx.Graph()
        relations = []

        for i in contents["graph"]["childs"]:
            relations.append(
                (contents["graph"]["name"], i["node"]["name"].replace(" ", "\n"), 1)
            )

        graph.add_weighted_edges_from(relations)

        nx.draw(graph, with_labels=True)
        nt = pv.network.Network(height="99vh")

        nt.from_nx(graph)

        nt.show(html)

        return GraphBuilderReturnCode.OK
