import unittest
import LowestCommonAncestor
from Node import Node

class testLowestCommonAncestor(unittest.TestCase):

    def test_LowestCommonAncestor(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        self.assertEqual(LowestCommonAncestor.findLowestCommonAncestor(root, 6, 7).key, 3)
        self.assertEqual(LowestCommonAncestor.findLowestCommonAncestor(root, 1, 7).key, 1)
        self.assertEqual(LowestCommonAncestor.findLowestCommonAncestor(root, 4, 5).key, 2)
        self.assertEqual(LowestCommonAncestor.findLowestCommonAncestor(root, 2, 5).key, 2)