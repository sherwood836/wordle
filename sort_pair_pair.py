def find_chain(pair_list):
    sorted_pair_list = sorted(pair_list)
    final_list = []

    if sorted_pair_list:
        final_list.append(sorted_pair_list[0])

        if len(sorted_pair_list) > 1:
            for idx in range(1, len(sorted_pair_list)):
                if final_list[-1][1] < sorted_pair_list[idx][0]:
                    final_list.append(sorted_pair_list[idx])

                elif final_list[-1][1] > sorted_pair_list[idx][1]:
                    final_list.pop()
                    final_list.append(sorted_pair_list[idx])


    return len(final_list)

import unittest

class FloydTest(unittest.TestCase):
    def test_find_chain(self):
        self.assertEqual(find_chain([[10, 30], [50, 65], [65, 80]]), 2)
        self.assertEqual(find_chain([[10, 30], [85, 100], [65, 80]]), 3)
        self.assertEqual(find_chain([]), 0)
        self.assertEqual(find_chain([[10, 30]]), 1)
        self.assertEqual(find_chain([[10, 30], [85, 100], [65, 80], [35, 55]]), 4)
        self.assertEqual(find_chain([[10, 30], [85, 100], [65, 80], [35, 85]]), 3)
        self.assertEqual(find_chain([[10, 30], [15, 20]]), 1)


if __name__ == "__main__":
    unittest.main()