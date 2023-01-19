def unique_find(search_string):
    char_list = [char for char in search_string]
    char_set = set(char_list)

    return len(char_list) == len(char_set)

def unique_find2(search_string):
    char_set = set()

    for char in search_string:
        if char in char_set:
            return False
        char_set.add(char)

    return True

def split_chocolate(m, n):
    split_count = m * n - 1

    return split_count

def divide_evenly(number, parts):
    closest_part = int(number / parts)
    bigger_num = number%parts

    part_list = [closest_part for _ in range(parts - bigger_num)]
    # part_list = part_list + [closest_part + 1 for _ in range(bigger_num)]
    part_list.extend([closest_part + 1 for _ in range(bigger_num)])

    return part_list

import unittest

class FloydTest(unittest.TestCase):
    def test_number_one(self):
        self.assertTrue(unique_find('asdfghjkl'))
        self.assertFalse(unique_find('aasdfghjkl'))

    def test_number_one2(self):
        self.assertTrue(unique_find2('asdfghjkl'))
        self.assertFalse(unique_find2('aasdfghjkl'))

    def test_number_two(self):
        self.assertEquals(split_chocolate(5, 5), 24)

    def test_number_three(self):
        self.assertEquals(divide_evenly(12, 2), [6, 6])
        self.assertEquals(divide_evenly(23, 5), [4, 4, 5, 5, 5])


if __name__ == "__main__":
    unittest.main()