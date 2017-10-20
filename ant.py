"""
Python implementation of Ant Colony Optimisation (ACO) meta-heuristic, for course requirements of CITS4404 @ University of Western Australia
"""
import random 
import math
import networkx as nx
import csv

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

    def __init__(self,id, depot=(0,0),capactiy=10):
        self._id = id
        self._solution = nx.Graph() # This is an empty graph
        self._depot = depot
        self._current = None
        self.capacity =  10

    def __repr__(self):
        return self._id


    def get_solution(self):
        return self._solution  
    

    def update_solution(self, next_customer):
        # Initialise the graph and add the depot to it; this should always happen the first time.
        if not self._solution:
            self._solution = nx.Graph()
            self._solution.add_node(self._depot)
            self._current = self._depot

        self._solution.add_node(next_customer)
        self._solution.add_edge(self._current,next_customer) 
        self._current = next_customer
        

    def get_current_position(self):
        if not self._current:
            return 'depot'

        return self._current

    def fitness_selection(self):
        return -1


class AntColony(object):
    def __init__(self,num_ants=5,alpha=1, beta=0.1,graph_file=None):
        self._graph = None
        self._iteration = 2
        self._ants = num_ants
        self._colony = []
        self._depot = (-1,0)

        self._q0 = 0.9 # most of the time, we use the pheromone
        self._alpha = alpha
        self._beta = beta
        self._pheromone_decay = 0.8
        self._unvisted_customers = None        

    def _init_ants(self):
        """
        This function initialises ants in the colony 
        """
        for x in range(0,self._ants):
            self._colony.append(Ant(x,self._depot,5))

        return self._colony

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
        demand = [4,5,12,7]
        for x in range(1,5):
            self._graph.node[x]['coord']=coords[x-1]
            self._graph.node[x]['demand'] = demand[x-1]

        # The list of unvisited customers 
        self._unvisted_customers = list(self._graph.nodes())

        # Initialise all edges on the graph, set the pheromone to 0
        self._graph.add_node('depot')
        self._graph.node['depot']['coord']=self._depot
        for node in self._graph:
            for other_node in self._graph:
                if other_node is not node:
                    self._graph.add_edge(node,other_node,pheromone=5)


        return self._graph 


    def csv_parser(self, graph_file=None):
        """
        graph_file = file path
        its assumed that 1st row will be contianing labels
        in order : CUST, NO.XCOORD., YCOORD.,DEMAND, READY TIME, DUE DATE, SERVICE TIME


        """
        self._graph = nx.Graph()

        #Reading from CSV, fetching data
        data = []
        try:
            with open(graph_file, 'rb') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=',')

                for i in csv_reader:
                    if not i[1].isdigit():
                        continue
                    else:
                        try:
                            temp = {}
                            temp["x_cord"] = i[1]
                            temp["y_cord"] = i[2]
                            temp["customer_id"] = i[0]
                            temp["demand"] = i[3]
                            data.append(temp)
                        except Exception as err:
                            pass                
        except Exception as err:
            
            return -1


        for i in data:
            self._graph.add_node(i["customer_id"],coord=(int(i["x_cord"]),int(i["y_cord"])),demand=int(i["demand"]))
        
        #Here I am setting pheromone value to 5 as i not clear about the config/structure that we will follow 
        self._graph.add_node('depot')
        self._graph.node['depot']['coord']=self._depot

        for node in self._graph:
            for other_node in self._graph:
                if other_node is not node:
                    self._graph.add_edge(node,other_node,pheromone=5)


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

        dist = math.sqrt(pow((c1x-c2x),2) + pow((c1y-c2y),2))
        print dist
        return int(dist)

    def roullette_wheel(self):
        """

        """        
        return -1

    def run(self):
        if not self._colony:
            self._init_ants()
            print("Successfully initialised ants")
        if not self._graph:
            self._init_graph()
            print("Successfully initialised graph")

        iteration_counter = 0
        if iteration_counter < self._iteration:
            self.do_next_iteration()
            iteration_counter = iteration_counter + 1 

    def do_next_iteration(self):

        for ant in self._colony:       
            soln = ant.get_solution()
            possible_customers = []
            best_customer = None
            
            while len(self._unvisted_customers) != 0: 
                for customer in self._unvisted_customers: 
                    if self._graph.node[customer]['demand'] > ant.capacity:
                        continue 
                    else: possible_customers.append(customer)            
                print ("possible_customers: "), (possible_customers)

                if not possible_customers:
                    # send the ant home! 
                    ant.update_solution('depot')
                    break

                # We need to reset the max pheromone values and next customer for each iteration over possible customers
                next_customer = None
                max_pheromone = -1 
                for customer in possible_customers:
                    #print ("Customer nr: "),(customer)
                    #print ("Customer's demand: "), (self._graph.node[customer]['demand'])
                    ant_pos = ant.get_current_position()
                    print self._graph
                    print(ant_pos)
                    edge_pheromone = self._graph[ant_pos][customer]['pheromone']
                    customer_coord = self._graph.node[customer]['coord']
                    ant_coord = self._graph.node[ant_pos]['coord']
                    dist = self.distance(ant_coord,customer_coord) 
                    q = random.random() 

                    if q < self._q0:
                        #print ("This is q: "), (q), ("compared to q0: "), (self._q0)
                        prob_formula = pow(edge_pheromone, self._alpha) * pow(1/float(dist), self._beta) 
                        #print ("Tau: "), (prob_formula)
                        if max_pheromone is -1:
                            max_pheromone = prob_formula
                            next_customer = customer
                        elif  max_pheromone < prob_formula:
                            max_pheromone = prob_formula
                            next_customer = customer 
                        else: continue  
                    else: 
                        print "Lets play roulette instead!"
                        next_customer = customer # THIS IS TEMPORARY SO IT DOESN'T FAIL
                print("Next customer is: {0}".format(customer))
                ant.capacity = ant.capacity - self._graph.node[next_customer]['demand']
                ant.update_solution(next_customer)
                self._unvisted_customers.remove(next_customer)
                possible_customers = [] # Need to reset the possible customers too, other wise we keep adding to the same list!
                print "New Ant capacity is: {0}".format(ant.capacity)     
            
            

if __name__ == "__main__": 
    aco = AntColony(10)
    aco.run()
 





