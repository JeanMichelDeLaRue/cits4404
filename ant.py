"""
Python implementation of Ant Colony Optimisation (ACO) meta-heuristic, for course requirements of CITS4404 @ University of Western Australia
"""
import random 
import math
import networkx as nx

"""
We can represent things differently now that we have are moving 
from the Moving Salesman to Vehicle Routing

What we need to represent: 
    - The routing graph (networkx object) [ACO Class]
    - The capacity of a vehicle (ant capactiy) [Ant Class]
    - The number of vehicles (num_ants) [ACO Class]
    - The unvisted nodes [ACO Class]
    - The number of iterations
    - {Optional} Maxmimum length travelled by an ant [Ant Class]
"""
        
class Ant(object): 

    def __init__(self, depot=(0,0),capactiy=10):
        self._solution = None # This is an empty graph
        self._depot = depot
        self._current = None

    def __repr__(self):
        return self._solution.nodes()


    def get_solution(self):
        return self._solution  
    # def 

    def update_solution(self, new_node):
        # Initialise the graph and add the depot to it; this should always happen the first time.
        if not self._solution:
            self._solution = nx.Graph()
            self._solution.add_node(self._depot)
            self._current = self._depot

        self._solution.add_node(new_node)
        self._solution.add_edge(self._current,new_node) 
        self._current = new_node

    def get_current_position(self):
        return self._current

    def fitness_selection(self):
        return -1


class AntColony(object):
    def __init__(self,num_ants=5,alpha=1, beta=0.1,graph_file=None):
        self._graph = None
        self._graph.edges[(1,2)]
        if self._graph.edge[(1,2)]:

        self._iteration = 0
        self._ants = num_ants
        self._colony = []

        self._q0 = 0.9 # most of the time, we use the pheromone
        self._alpha = alpha
        self._beta = beta
        self._pheromone_decay = 0.8
        self._unvisted_customers = None        

    def _init_ants(self):
        """
        This function initialises ants in the colony 
        """

        return -1

    def _init_graph(self, graph_file=None):
        """
        How the graph is constructed:

        graph = nx.Graph() initialises an empty graph
        graph.add_node(1) will add '1' to the graph

        For our purposes, we can also add other attributes
        graph.add_node(1,coord=(45,60),demand=17)

        We then access nodes and their coordinates like this: 
        >>  In[1]: graph.node[1]
        >> Out[1]: {'coord':(45,60), 'demand':17}
        """

        # TODO - Read in the graph from the CSV file

        # CONSTRUCT A TEMPORARY, SMALL GRAPH

        self._graph = nx.Graph()
        self._graph.add_nodes_from([1,2,3,4]) 
        coords = [(45,60),(-45,60),(45,-60),(-45,-60)]
        demand = [4,5,6,7]
        for x in range(1,5):
            self._graph.node[x]['coord']=coords[x-1]
            self._graph.node[x]['demand'] = demand[x-1]

        self._unvisted_customers = list(self._graph.nodes())

        return self._graph 


    def global_pheromone_update(self):
        """
        This function decays the pheromones on the trail
        """
        return -1 

    def distance(self, c1, c2):
        """
        Calculate the distance between the coordinates of 2 vertices
        :param c1: The coordinate tuple of the first vertex
        :param c2: The coordinate tuple of the second vertex
        """

        c1x,c1y = c1
        c2x,c2y = c2

        dist = math.sqrt(pow((c2x-c1x),2) + pow((c2y-c1y),2))

        return int(dist)

    def run(self):
        if not self._colony:
            self._init_ants()
        if not self._graph:
            self._init_graph()

        for ant in self._colony:
            soln = ant.get_solution()
            while len(soln) < len(self._graph):
                for customer in self._unvisted_customers:
                    if not ant.get_solution:
                        curren_pos = ant._depot
                    tau = self._graph.edge[ant.current][customer]['pheremone']
                    # What variables we need
                    edge_pheromone = - 1
                    inverse_distance = -1 
                    self._beta 
                    q = random.random()

        return -1  


if __name__ == "__main__": 
    aco = AntColony(10)
    aco.run()
    """
    TODO:
    Have the Ant colony 'run' over n iterations
        - Iteration starts from ant colony object
        - The approach to finding a path between each moving target 
        can just involve randomly grabbing a target and adding it as a node to the graph  
        -  likewise, pheromones can just be the actual distance (pheromones become edge weights on the graph)
        -  each iteration means that the targets move - update these targets each iteration 
        - display final results

    """


