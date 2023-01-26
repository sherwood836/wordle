def find_intersect(list_input, search_value):
    list_dict = {}

    for line in list_input.split("\n"):
        if "->" in line:
            key, value = line.split("->")
            list_dict[key] = value

    head_list = search_value.split(",")
    node_set = set()
    found_value = False

    for head in head_list:
        curr = head

        while curr:
            if curr in node_set:
                found_value = True
            
            node_set.add(curr)
            curr = list_dict.get(curr)

    return found_value


import unittest

class FloydTest(unittest.TestCase):
    def test_find_intersect(self):
        input = '''a->b
b->c
z->x
x->y
w->c
'''
        self.assertFalse(find_intersect(input, "a,x"))
        self.assertTrue(find_intersect(input, "a,w"))


if __name__ == "__main__":
    unittest.main()