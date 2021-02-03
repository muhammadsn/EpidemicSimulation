from random import *
import numpy as np
from NetworkGen import NetworkGenerator as NG
from Monitor import Monitor


class Simulator:
    network = None
    N = 0
    X = 0
    Y = 0
    susceptible = dict()
    infected = dict()
    p_infect = 0.0
    max_time_steps = 0
    monitor = Monitor()

    def __init__(self, params):
        self.X = params['X']
        self.Y = params['Y']
        self.network = NG(params['X'], params['Y'], params['DELTA'])
        first_infected = self.set_initial_infected()
        self.p_infect = params['BETA']
        self.max_time_steps = params['MaxTimeSteps']
        self.susceptible = {0: self.network.get_nodes_with_attr("I", False)}
        self.infected = {0: self.network.get_nodes_with_attr("I", True)}
        print(self.infected)

    def simulate(self):
        for t in range(1, self.max_time_steps):
            new_susceptible_neighbors = []
            for n in self.infected[t - 1]:
                sn = self.network.get_node_neighbours(n)
                for s in sn:
                    if s not in new_susceptible_neighbors and s not in self.infected[t - 1]:
                        new_susceptible_neighbors.append(s)

            self.infect(new_susceptible_neighbors)

            self.susceptible[t] = self.network.get_nodes_with_attr("I", False)
            self.infected[t] = self.network.get_nodes_with_attr("I", True)
            a = self.monitor.show_network(self.network, self.X, self.Y, t)
            # print(len(self.infected[t]))
            # print(len(self.susceptible[t]))
            # print(t, "\t=========================================")

    def set_initial_infected(self):
        d_min = 1
        first_infected = 0
        nodes = self.network.get_nodes()
        X = self.network.get_Map_X()
        Y = self.network.get_Map_Y()
        for n in nodes:
            x, y = nodes[n]
            d = (x - X / 2) ** 2 + (y - Y / 2) ** 2
            if d < d_min:
                first_infected = n
                d_min = d
        self.network.set_node_attr({first_infected: True}, "I")
        return first_infected

    def infect(self, neighbour_list):
        if len(neighbour_list):
            # next_infected = []
            # for i in neighbour_list:
            #     if random() <= self.p_infect:
            #         next_infected.append(i)
            # Inf = dict.fromkeys(next_infected)

            next_infected = choices(neighbour_list, weights=[self.p_infect/len(neighbour_list) for x in range(len(neighbour_list))], k=len(neighbour_list))
            Inf = dict.fromkeys(next_infected)

            for n in Inf:
                Inf[n] = True
            print(Inf)
            self.network.set_node_attr(Inf, "I")
