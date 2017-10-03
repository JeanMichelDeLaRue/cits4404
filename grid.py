"""
Python implementation of Ant Colony Optimisation (ACO) meta-heuristic, for course requirements of CITS4404 @ University of Western Australia
"""
import random 
import networkx as nx
class Target(object):

    def __init__(self,tid, xinit, yinit):
        self._tid = tid
        self._init_pos = (xinit, yinit)     
        self._current_pos = (xinit,yinit)
        self._velocity = (random.randint(1,xinit),random.randint(1,yinit)) 

    def __repr__(self):
        return self._tid

    def current_position(self):
        return self._current_pos

    def velocity(self):
        return self._velocity

    def update_position(self,x,y,gridx,gridy,iteration):
        """
        We need to update the position of the target after an iteration
        """
        return -1 
        

class Grid(object):

    def __init__(self, xmax=500, ymax=500, target_list=[],num_targets=10): 
        self._gridx = xmax
        self._gridy = ymax

        # List of Target objects that are currently populating the grid 
        if target_list:
            self._target_list = target_list
        else: 
            self._target_list = []

    def __len__(self):
        return len(self._target_list)

    def size(self):
        return (self._gridx,self._gridy)

    def add_target_to_grid(self,target):
        self._target_list.append(target)
    
        
    def distance(self, t1, t2):
        return -1 

    def targets(self):
        return self._target_list

    def state(self):
        for target in self._target_list:
            x,y = target.current_position()
            print("{0}: ({1},{2})\t".format(target,x,y))


class Ant(object): 

    def __init__(self, target):
        self._target = target
        self._solution = nx.Graph() # This is graph
        self._previous = None

    def __repr__(self):
        return self._solution.nodes()

    def current_position(self):
        return self._target.current_position()

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
    def __init__(self,grid,num_ants=25,alpha=1, beta=0.1):
        self._grid = grid 
        self._iteration = 0
        self._ants = num_ants
        self._colony = []
        self._alpha = alpha
        self._beta = beta
        # self._pheromone = 0


    def _init_ants(self):
        """
        This function initialises ants in the colony 
        """
        grid_size = len(self._grid)
        for i in range(0,self._ants):
            index = random.randint(0,grid_size-1)
            target = grid.targets()[index]

            ant = Ant(target)   
            self._colony.append(ant)    
        return -1 

    def grid_state(self):
        return self._grid.state()

    def run(self):
        if not self._colony:
            self._init_ants()

        for ant in self._colony:
            max_solution = 0 
            print ant.current_position()
            target_list = self._grid.targets()
            current_solution = ant.get_solution()
            previous_node = None
            count = 1 
            while len(current_solution) < len(self._grid):
                """
                This is where the pheremone/path selection occurs - not implemented yet
                """ 
                index = random.randint(0,len(self._grid)-1)
                target = target_list[index]                
                gridx, gridy = self._grid.size()
                x,y = target.current_position()
                target.update_position(x,y,gridx,gridy,count)
                if target not in current_solution:
                    ant.update_solution(target)
                count = count + 1    

        """
        Running the simulations follows the following structure:
        1. Each ant constructs a solution
        2. Ants lay pheremones on the solution path
        3. After all pheremones are laid, we evaporate according to the evaporation rate
        """ 
        return -1  


if __name__ == "__main__": 
    targetA = Target("A",5,5)
    targetB = Target("B",1,6)
    targetC = Target("C",7,8)

    grid = Grid(250,250,[targetA,targetB,targetC])
    # grid.state()    

    aco = AntColony(grid,10)
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


