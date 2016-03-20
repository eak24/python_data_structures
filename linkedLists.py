class Node:
    def __init__(self, left_node, right_node):
        self.left_node=left_node
        self.right_node=right_node

def findLoop(head_node):
    fast_node=head_node.left_node
    slow_node=head_node.left_node
    while fast_node.left_node != None and slow_node !=None:
        if slow_node == fast_node:
            return slow_node
        fast_node=fast_node.left_node.leftnode
        slow_node=slow_node.left_node
    return None

import unittest
class TestLinkedLists(unittest.TestCase):
    e = Node(None,None)
    f = Node(e,None)
    g = Node(f,None)
    h = Node(g, None)
    i = Node(h, None)
    e.left_node=g
    def test_has_loop_true(self):
        self.assertNotEqual(findLoop(TestLinkedLists.e),None)
    def test_has_loop_true(self):
        self.assertEqual(findLoop(TestLinkedLists.e),TestLinkedLists.g)

if __name__=='__main__':
    unittest.main()