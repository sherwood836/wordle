def join_list(l1, l2):
    new_list = []
    new_list.extend(l1)
    new_list.extend(l2)
    new_list = sorted(new_list)

    return_list = []

    if len(new_list) > 1:
        prev = 0

        for curr in range(1, len(new_list)):
            if new_list[prev][0] == new_list[curr][0]:
                return_list.append((new_list[prev][0], new_list[prev][1], new_list[curr][1]))

            prev = curr

    return return_list

def join_list_of_list(list_of_list):
    new_list = []
    for each_list in list_of_list:
        new_list.extend(each_list)
    new_list = sorted(new_list)

    return_list = []

    if len(new_list) > 1:
        prev = 0
        last_key = new_list[prev][0]
        last_key_value_list = [new_list[prev][1]]

        for curr in range(1, len(new_list)):
            if last_key == new_list[curr][0]:
                last_key_value_list.append(new_list[curr][1])
            else:
                if len(last_key_value_list) == len(list_of_list):
                    new_tuple = tuple([last_key] + [value for value in last_key_value_list])
                    return_list.append(new_tuple)
                last_key = new_list[curr][0]
                last_key_value_list = [new_list[curr][1]]

            prev = curr

    return return_list


import unittest

class FloydTest(unittest.TestCase):
    def test_join_list(self):
        list1 = [("k1", "v1"), ("k2", "v2")]
        list2 = [("k2", "v3"), ("k3", "v4")]

        self.assertEqual(join_list(list1, list2), [("k2", "v2", "v3")])
        # list1 = [("k1", "v1"), ("k2", "v2")]
        list2 = [("k3", "v4"), ("k2", "v3"), ]
        self.assertEqual(join_list(list1, list2), [("k2", "v2", "v3")])

    def test_join_list_of_list(self):
        list1 = [("k1", "v1"), ("k2", "v2")]
        list2 = [("k2", "v3"), ("k3", "v4")]

        list_of_list = [list1, list2]
        self.assertEqual(join_list_of_list(list_of_list), [("k2", "v2", "v3")])
        list1 = [("k1", "v1"), ("k2", "v2")]
        list2 = [("k3", "v4"), ("k2", "v3"), ]
        list_of_list = [list1, list2]
        self.assertEqual(join_list_of_list(list_of_list), [("k2", "v2", "v3")])


if __name__ == "__main__":
    unittest.main()