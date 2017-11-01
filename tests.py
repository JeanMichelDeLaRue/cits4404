"""
Tests for ant.py
"""
import random 
import unittest

import networkx as nx

from ant import Ant, AntColony

class TestAntMethods(unittest.TestCase):
    def setUp(self):
        self.ant = Ant(1)
        

    def tearDown(self):
        return -1

    def testGetSolution(self):
        self.ant.update_solution('1')
        print self.ant._solution.edges()
        # self.ant.update_solution('2')
        # print self.ant._solution.edges()
        self.ant.update_solution('depot')
        print self.ant._solution.edges()    



class TestAntColonyMethods(unittest.TestCase):
    def setUp(self):
        self.aco = AntColony(100) 

    def tearDown(self):
        return -1

    def testInitAnts(self):
        colony = self.aco._init_ants()
        self.assertTrue(len(colony) is 15)

    def testInitGraphNoFile(self):
        graph = self.aco._init_graph()   

        self.assertTrue(1 in graph)
        self.assertFalse(7 in graph)
        coord = graph.node[3]['coord']

        self.assertTrue(coord[0] is 45)
        self.assertTrue(graph.node['depot'])
        self.assertTrue(graph.node[2]['demand'] is 5)
        self.assertTrue(graph[1][2]['pheromone'] is 5)
        self.assertTrue(graph[2][1])
        self.assertTrue(graph[3][1])

    def testDistance(self):
        c1 = (1,2)
        c2 = (5,5)

        retval = self.aco.distance(c1,c2)
        self.assertFalse(retval is 7)
        self.assertTrue(retval is 5)

        c1 = (45,60)
        c2 = (-45,60)

        retval = self.aco.distance(c1,c2)
        self.assertTrue(retval is 90)
        c1 = (45,60)
        c2 = (-45,-60)

        retval = self.aco.distance(c1,c2)
        self.assertTrue(retval is 150)


    def testCustomerDistance(self):
        graph = self.aco._init_graph()
        customers = self.aco._unvisted_customers
        print customers
        customer1 = graph.node[customers[0]]
        self.assertTrue(customer1['coord'][1] is 60)

    def testCSVParser(self):
        graph = self.aco.csv_parser('example.csv')
        self.assertTrue(graph.node['1']['coord'][0] is 40)
        self.assertTrue(graph.node['1']['coord'][1] is 50)
        self.assertTrue(graph.node['92']['demand'] is 10)
        self.assertTrue(graph['1']['2']['pheromone'] is 5)
        # self.assertTrue(graph['1'][])

    def testRun(self):
        ret_list = self.aco.run()
        print ret_list

    def testRoulette(self):
        graph = self.aco.csv_parser('example.csv')
        self.aco.run()

    def testDecay(self):
        graph = self.aco.csv_parser('example.csv')
        for edge in graph.edges():
            self.aco.pheromone_decay(edge)
            print graph[edge[0]][edge[1]]['pheromone'] 