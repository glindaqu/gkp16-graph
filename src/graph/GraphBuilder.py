from yaml_parser.YamlParser import YamlParser
from graph.GraphBuilderException import GraphBuilderException
from yaml_parser.YamlParserReturnCode import YamlParserReturnCode
import pyvis as pv
import networkx as nx


class GraphBuilder:
    def build(self, yaml, html):
        self.parser = YamlParser()
        result = self.parser.build(yaml)

        if result == YamlParserReturnCode.PERMISSION_DENIED:
            raise GraphBuilderException.PERMISSION_DENIED
        elif result == YamlParserReturnCode.FILE_DOES_NOT_EXISTS:
            raise GraphBuilderException.FILE_DOES_NOT_EXISTS

        contents = self.parser.get_contents()

        graph = nx.Graph()
        relations = []

        for i in contents['graph']['childs']:
            relations.append((contents['graph']['name'], i['node']['name'], 1))

        graph.add_weighted_edges_from(relations)

        nx.draw(graph, with_labels=True)
        nt = pv.network.Network()
        nt.from_nx(graph)
        nt.show(html)

        return contents
