import networkx as nx
import matplotlib.pyplot as plt


class Monitor:
    simulation = None
    simulation_network = None

    def __init__(self):
        pass

    def show_network(self, simulation, X, Y, t):
        self.simulation = simulation
        self.simulation_network = simulation.get_network()
        nodes = self.simulation.get_nodes()
        node_color_map = []
        for node in self.simulation_network:
            if self.simulation.get_node_attr(node, "I"):
                node_color_map.append('#ff0000')
            else:
                node_color_map.append('#000000')

        plt.figure(figsize=(5, 5))
        # nx.draw(                  # If you want to see edges for simulated network uncomment this line
        nx.draw_networkx_nodes(     # and comment this line (not recommended though)
            self.simulation_network,
            nodes,
            nodelist=list(nodes.keys()),
            node_size=20,
            node_color=node_color_map,
            # with_labels=True      # Uncomment to see nodes' numbers on map
        )

        plt.xlim(0, X)
        plt.ylim(0, Y)
        xticks = [x for x in range(X)]
        yticks = [x for x in range(Y)]
        plt.xticks(ticks=xticks)
        plt.yticks(ticks=yticks)
        plt.title(f"Infected Nodes in t = {str(t)}")
        plt.grid()
        plt.show()
