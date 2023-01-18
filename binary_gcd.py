def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a%b)

def find_gcd_and_node(node):
    max_gcd = None
    max_node_value = None

    if node.left and node.right:
        if node.left:
            left_value, left_node_value = find_gcd_and_node(node.left)

        if node.right:
            right_value, right_node_value = find_gcd_and_node(node.right)

        max_gcd = gcd(node.left.value, node.right.value)
        max_node_value = node.value

        if right_value is not None:
            if right_value > max_gcd:
                max_gcd = right_value
                max_node_value = right_node_value

        if left_value is not None:
            if left_value > max_gcd:
                max_gcd = left_value
                max_node_value = left_node_value

    return max_gcd, max_node_value

def maxGCD(node):
    return find_gcd_and_node(node)

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

import unittest

class FloydTest(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(4, 8), 4)
        self.assertEqual(gcd(8, 4), 4)

    def test_binary_gcd(self):
        node6 = Node(6)
        node9 = Node(9)
        node8 = Node(8)
        node4 = Node(4)
        node5 = Node(12)
        node3 = Node(6)
        node1 = Node(1)
        node3.left = node6
        node3.right = node9
        node5.left = node4
        node5.right = node8
        node1.left = node3
        node1.right = node5

        self.assertEqual(maxGCD(node1), (6, 1))

    def test_binary_gcd2(self):
        node6 = Node(6)
        node9 = Node(9)
        node8 = Node(8)
        node4 = Node(4)
        node5 = Node(5)
        node3 = Node(3)
        node1 = Node(1)
        node3.left = node6
        node3.right = node9
        node5.left = node4
        node5.right = node8
        node1.left = node3
        node1.right = node5

        self.assertEqual(maxGCD(node1), (4, 5))


if __name__ == "__main__":
    unittest.main()