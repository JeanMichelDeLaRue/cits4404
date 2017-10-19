"""
Tests for ant.py
"""
import random 
import unittest

import networkx as nx

from ant import Ant, AntColony

class TestAntMethods(unittest.TestCase):
    def setUp(self):
        return -1   

    def tearDown(self):
        return -1

class TestAntColonyMethods(unittest.TestCase):
    def setUp(self):
        self.aco = AntColony(15) 

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

    def testRun(self):
        ret_list = self.aco.run()
        print ret_list

