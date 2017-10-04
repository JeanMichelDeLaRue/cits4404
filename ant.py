"""
Python implementation of Ant Colony Optimisation (ACO) meta-heuristic, for course requirements of CITS4404 @ University of Western Australia
"""
import random 
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

# class Target(object):

#     def __init__(self,tid, xinit, yinit):
#         self._tid = tid self._init_pos = (xinit, yinit)
#         self._current_pos = (xinit,yinit)
#         self._velocity = (random.randint(1,xinit),random.randint(1,yinit)) 

#     def __repr__(self):
#         return self._tid

#     def current_position(self):
#         return self._current_pos

#     def velocity(self):
#         return self._velocity

#     def update_position(self,x,y,gridx,gridy,iteration):
#         """
#         We need to update the position of the target after an iteration
#         """
#         return -1 
        
class Ant(object): 

    def __init__(self, target):
        self._solution = nx.Graph() # This is an empty graph
        self._previous = None

    def __repr__(self):
        return self._solution.nodes()


    def get_solution(self):
        return self._solution  
    # def 

    def update_solution(self, new_node,distance=None):
        if not self._previous:
            self._previous = new_node
            self._solution.add_node(new_node)
        else:
            self._solution.add_node(new_node)
            self._solution.add_edge(self._previous,new_node,weight=distance)
            self._previous = new_node

    def fitness_selection(self):
        return -1


class AntColony(object):
    def __init__(self,num_ants=25,alpha=1, beta=0.1,graph_file=None):
        self._graph = self._init_graph(graph_file) 

        self._iteration = 0
        self._ants = num_ants
        self._colony = []
        self._alpha = alpha
        self._beta = beta
        self._pheremone_decay = 0.8


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
        return -1 


    def global_pheremone_update(self):
        """
        This function decays the pheremones on the trail
        """
        return -1 

    def run(self):
        if not self._colony:
            self._init_ants()

        """
        Running the simulations follows the following structure:
        1. Each ant constructs a solution
        2. Ants lay pheremones on the solution path
        3. After all pheremones are laid, we evaporate according to the evaporation rate
        """ 
        return -1  


if __name__ == "__main__": 
    # targetA = Target("A",5,5)
    # targetB = Target("B",1,6)
    # targetC = Target("C",7,8)

    # grid.state()    

    aco = AntColony(10)
    # aco.grid_state()
    aco.run()
    """
    TODO:
    Have the Ant colony 'run' over n iterations
        - Iteration starts from ant colony object
        - ants are initialised to random city from the grid
        - The approach to finding a path between each moving target 
        can just involve randomly grabbing a target and adding it as a node to the graph  
        -  likewise, pheremones can just be the actual distance (pheremones become edge weights on the graph)
        -  each iteration means that the targets move - update these targets each iteration 
        - display final results

    """


