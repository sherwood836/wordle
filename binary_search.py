
def find_index(search_list, value, base_index = 0):
    mid_index = int(len(search_list) / 2)

    if len(search_list) == 1 and value != search_list[0]:
        return None

    print(f"value: {value}, search_list: {search_list}, mid_index: {mid_index}, base_index: {base_index}")
    if value > search_list[mid_index]:
        return find_index(search_list[mid_index:], value, mid_index + base_index)
    elif value < search_list[mid_index]:
        return find_index(search_list[:mid_index], value, base_index)
    elif value == search_list[mid_index]:
        return mid_index + base_index

    return None

import unittest

class FloydTest(unittest.TestCase):
    def test_has_loop2(self):
        search_list = [1, 2, 3, 4, 5]

        self.assertEquals(find_index(search_list, 4), 3)

    def test_has_loop1(self):
        search_list = [1, 2, 3, 4, 5]

        self.assertEquals(find_index(search_list, 1), 0)

    def test_has_loop22(self):
        search_list = [1, 2, 3, 4, 5]

        self.assertEquals(find_index(search_list, 2), 1)

    def test_has_loop3(self):
        search_list = [1, 2, 3, 4, 5]

        self.assertEquals(find_index(search_list, 3), 2)


    def test_has_loop400(self):
        search_list = [1, 2, 3, 4, 5]

        self.assertEquals(find_index(search_list, 400), None)

    def test_has_loop100(self):
        search_list = [i for i in range(1, 100)]

        self.assertEquals(find_index(search_list, 45), 44)


if __name__ == "__main__":
    unittest.main()