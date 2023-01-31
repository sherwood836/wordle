def find_intersect(list_input, search_value):
    list_dict = {}

    for line in list_input.split("\n"):
        if "->" in line:
            key, value = line.split("->")
            list_dict[key] = value

    head_list = search_value.split(",")
    node_set = set()
    found_value = False

    for head in head_list:  # line 13
        curr = head
        traverse_node_set = set()

        if not found_value:
            while curr and curr not in traverse_node_set:   # line 16
                if curr in node_set:  # line 17
                    found_value = True
                    break
                
                node_set.add(curr)
                traverse_node_set.add(curr)
                curr = list_dict.get(curr)

    return found_value


import unittest
import timeit
import string

input = '\n'.join([f'{char[0]}->{char[1]}' for char in zip(string.ascii_lowercase[:-1], string.ascii_lowercase[1:])]) + "\nz->d"

class FloydTest(unittest.TestCase):
    def test_find_intersect(self):

        print(timeit.timeit('find_intersect(input, "a,a")', setup="from __main__ import find_intersect, input",  number=10000))
        print(timeit.timeit('find_intersect(input, "a,m")', setup="from __main__ import find_intersect, input",  number=10000))
        print(timeit.timeit('find_intersect(input, "a,x")', setup="from __main__ import find_intersect, input",  number=10000))

        input = '\n'.join([f'{char[0]}->{char[1]}' for char in zip(string.ascii_lowercase[:-1], string.ascii_lowercase[1:])])
        input += "\nz->d"
        print(input)
        self.assertTrue(find_intersect(input, "a,x"))
        self.assertTrue(find_intersect(input, "a,w"))


if __name__ == "__main__":
    unittest.main()