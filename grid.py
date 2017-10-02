"""
Python implementation of Ant Colony Optimisation (ACO) meta-heuristic, for course requirements of CITS4404 @ University of Western Australia
"""
import random 
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

    def update_position(self):
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

    def add_target_to_grid(self,target):
        self._target_list.append(target)
    
    def update_target_position(self,target): 
       return -1  
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
        self.rand_target = target
        self.solution = None # This is graph

    def fitness_selection(self):
        return -1


class AntColony(object):
    def __init__(self,grid,num_ants=25,alpha=1, beta=0.1):
        self._grid = grid 
        self._iteration = 0
        self._colony = []
        self._alpha = alpha
        self._beta = beta
        self._pheromone = 0


    def _init_ants(self, num_ants):
        """
        This function initialises ants in the colony 
        """
        for i in range(0,num_ants):
            target = self.grid 
        return -1 

    def grid_state(self):
        return self._grid.state()

    def run(self):
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
    grid.state()    

    aco = AntColony(grid,10)
    aco.grid_state()

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


