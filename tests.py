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


    def testInitGraphNoFile(self):
        graph = self.aco._init_graph()   

        self.assertTrue(1 in graph)
        self.assertFalse(7 in graph)
        coord = graph.node[3]['coord']

        self.assertTrue(coord[0] is 45)
        self.assertTrue(graph.node[2]['demand'] is 5)

    def testDistance(self):
        c1 = (1,2)
        c2 = (5,5)

        retval = self.aco.distance(c1,c2)
        self.assertFalse(retval is 7)

    