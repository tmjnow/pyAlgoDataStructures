"""
 Name: Gravity Tree

 Ref: https://www.hackerrank.com/contests/w23/challenges/gravity-1
"""
import unittest


def construct_tree(nodes, node_connections):
    tree = {}
    return tree


def gravity_tree(tree, u, v):
    pass


class MyTestCases(unittest.TestCase):
    def test_gravity_tree(self):
        n = 5
        node_connections = [1, 2, 2, 4]
        tree = construct_tree(n, node_connections)
        u, v = 2, 1
        self.assertEqual(gravity_tree(tree, u, v), 7)
        u, v = 1, 4
        self.assertEqual(gravity_tree(tree, u, v), 13)
