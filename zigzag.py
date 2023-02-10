def zig_zag(node, direction):
    s1 = []
    s2 = []
    return_list = []

    if node:
        if direction:
            s2.append(node)
        else:
            s1.append(node)
    
        while s1 or s2:
            if direction:
                this_node = s2.pop()
                return_list.append(this_node.value)
                if this_node.left: s1.append(this_node.left)
                if this_node.right: s1.append(this_node.right)
                if not s2: direction = not direction
            else:
                this_node = s1.pop()
                return_list.append(this_node.value)
                if this_node.right: s2.append(this_node.right)
                if this_node.left: s2.append(this_node.left)
                if not s1: direction = not direction


    return return_list


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def make_node(arr, indx):
  node = Node(arr[indx])

  if indx * 2 + 1 < len(arr) and arr[indx * 2 + 1] != -1:
    node.left = make_node(arr, indx * 2 + 1)
  if indx * 2 + 2 < len(arr) and arr[indx * 2 + 2] != -1:
    node.right = make_node(arr, indx * 2 + 2)

  return node


import unittest

class FloydTest(unittest.TestCase):
    def test_zigzag(self):
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

        '''
      1
    /  \
   6    12
  / \   / \
 6   9 4   8
'''

        self.assertEqual(zig_zag(node1, True), [1, 12, 6, 6, 9, 4, 8])
        self.assertEqual(zig_zag(node1, False), [1, 6, 12, 8, 4, 9, 6])

    def test_zigzag2(self):
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

        self.assertEqual(zig_zag(node1, True), [1, 5, 3, 6, 9, 4, 8])
        self.assertEqual(zig_zag(node1, False), [1, 3, 5, 8, 4, 9, 6])


    # def test_binary_big_tree(self):
    #     big_list = [(num * (num + 1)) for num in range(1, 2**5)]
    #     node32 = make_node(big_list, 0)
    #     self.assertEqual(maxGCD(node32), (62, 240))

    #     big_list = [(num * (num + 1)) for num in range(1, 2**6)]
    #     node32 = make_node(big_list, 0)
    #     self.assertEqual(maxGCD(node32), (126, 992))


if __name__ == "__main__":
    unittest.main()

'''
Problem: Print Zigzag output for a Binary tree

     10
    /  \
   5    15
  / \   / \
 2   3 11  20

Expected output:
  10    5    15   20   11   3   2. (direction =true)
  10.   15.  5.   2.   3.   11.  20

s1 = [ 10 ]
s1 = [10, 5, 15]
s1 = '    '.[10, 5, 15, 20, 11 ]

output: 10   15  5 2 3 11 20
s1 = [ 15, ]
s2 = [ 10 ]


Consider this Employees table:
empid, Name,  Title,      Update_time
 1     John   Engineer      10/2/2016
 2     Beth   Hr Assnt      05/4/2017
 1     John   Sr. Engineer  12/1/2018
 1     John   Manager       09/2/2019
 2     Beth   Hr Mgr        05/4/2018

 - Find the number of times titles seen for John
select empid, Name, count(*) from Employee
group by empid

'''

# class Node():
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# def zigzag_tree(node_instance, direction):
#     s1 = []
#     s2 = []
    
#     if node_instance:
#         if direction:
#             s2.append(node_instance)
#         else:
#             s1.append(node_instance)
        
#         while s2 or s1:
#             if direction:
#                 this_node = s2.pop()
#                 print(this_node.data)
#                 if this_node.right: s1.append(this_node.right)
#                 if this_node.left: s1.append(this_node.left)
#                 if not s2:
#                     direction = not direction
#             elif not direction:
#                 this_node = s1.pop()
#                 print(this_node.data)
#                 if this_node.left: s2.append(this_node.left)
#                 if this_node.right: s2.append(this_node.right)
#                 if not s1:
#                     direction = not direction

        
# if __name__ == '__main__':
#     node_instance = Node(10)
#     node_instance.left = Node(5)
#     node_instance.right = Node(15)
#     node_instance.left.left = Node(2)
#     node_instance.left.right = Node(3)
#     node_instance.right.left = Node(11)
#     node_instance.right.right = Node(20)
#     zigzag_tree(node_instance, True)
#     print('*******')
#     zigzag_tree(node_instance, False)


