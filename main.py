from graph.GraphBuilder import GraphBuilder


def main():
    graph_builder = GraphBuilder()
    graph_builder.build("data/struct.yaml", "output/graph.html")


if __name__ == "__main__":
    main()
