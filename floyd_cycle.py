
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

def find_loop(node):
    slow = node
    fast = node

    while slow and fast and fast.next:
        print(f"1 slow: {slow.data}, fast: {fast.data}")
        slow = slow.next
        fast = fast.next.next

        if slow and fast:
            print(f"2 slow: {slow.data}, fast: {fast.data}")
        if slow == fast:
            break

    if slow != fast:
        return False
    
    slow = node
    while slow != fast:
        print(f"3 slow: {slow.data}, fast: {fast.data}")
        slow = slow.next
        fast = fast.next

    return slow

import unittest

class FloydTest(unittest.TestCase):
    def test_has_loop2(self):
        node6 = Node(6, None)
        node5 = Node(5, node6)
        node4 = Node(4, node5)
        node3 = Node(3, node4)
        node2 = Node(2, node3)
        node1 = Node(1, node2)
        node6.next = node2

        self.assertEquals(find_loop(node1), node2)

    def test_has_loop3(self):
        node6 = Node(6, None)
        node5 = Node(5, node6)
        node4 = Node(4, node5)
        node3 = Node(3, node4)
        node2 = Node(2, node3)
        node1 = Node(1, node2)
        node6.next = node3

        self.assertEquals(find_loop(node1), node3)

    def test_has_loop4(self):
        node6 = Node(6, None)
        node5 = Node(5, node6)
        node4 = Node(4, node5)
        node3 = Node(3, node4)
        node2 = Node(2, node3)
        node1 = Node(1, node2)
        node6.next = node4

        self.assertEquals(find_loop(node1), node4)

    def test_has_no_loop(self):
        node6 = Node(6, None)
        node5 = Node(5, node6)
        node4 = Node(4, node5)
        node3 = Node(3, node4)
        node2 = Node(2, node3)
        node1 = Node(1, node2)

        self.assertFalse(find_loop(node1))

if __name__ == "__main__":
    unittest.main()