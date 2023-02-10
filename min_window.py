def min_matrix(input, k):
  ret_mat = []
  for row in input:
    ret_mat.append(min_window(row, k))
  
  transpose_mat = []
  for cindex in range(len(ret_mat[0])):
      transpose_mat.append([])

  for rindex in range(len(ret_mat)):
    for cindex in range(len(ret_mat[rindex])):
      transpose_mat[cindex].append(ret_mat[rindex][cindex])

  # print(transpose_mat)

  need_transpose_mat = []

  for row in transpose_mat:
    need_transpose_mat.append(min_window(row, k))

  # print(need_transpose_mat)

  transpose_mat = []
  for cindex in range(len(need_transpose_mat[0])):
      transpose_mat.append([])

  for rindex in range(len(need_transpose_mat)):
    for cindex in range(len(need_transpose_mat[rindex])):
      transpose_mat[cindex].append(need_transpose_mat[rindex][cindex])

  # print(transpose_mat)

  return transpose_mat


def min_window(input, k):
  ret_list = []
  window = []

  for index in range(len(input)):
    while window and input[window[-1]] > input[index]:
      window.pop()

    window.append(index)

    if window[0] == index - k:
       window.pop(0)
    if index > k - 2:
       ret_list.append(input[window[0]])

  return ret_list

def max_window(input, k):
  ret_list = []
  window = []

  for index in range(len(input)):
    while window and input[window[-1]] < input[index]:
      window.pop()

    window.append(index)

    if window[0] == index - k:
       window.pop(0)
    if index > k - 2:
       ret_list.append(input[window[0]])

  return ret_list


import unittest

class MinWindowTest(unittest.TestCase):
    def test_min_window(self):
        self.assertEqual(min_window([3, 2, 1, 4, 5, 2, 6, 3, 5], 3), [1, 1, 1, 2, 2, 2, 3])
        self.assertEqual(min_window([3, 2, 1, 4, 5], 2), [2, 1, 1, 4])
        self.assertEqual(min_window([2, 2, 5, 4], 2), [2, 2, 4])
        self.assertEqual(min_window([1, 2, 3, 4, 5, 6, 7], 3), [1, 2, 3, 4, 5])
        self.assertEqual(min_window([7, 5, 4, 3, 6, 5, 2, 5, 4, 1], 3), [4, 3, 3, 3, 2, 2, 2, 1])

    def test_min_matrix(self):
        self.assertEqual(min_matrix([[3, 2, 1, 4], [5, 2, 6, 3], [5, 8, 9, 5], [4,5,6,7]], 2),
        [[2, 1, 1], [2, 2, 3], [4, 5, 5]])
        self.assertEqual(min_matrix([[3, 2, 1, 4, 6], [5, 2, 6, 3, 7], [5, 8, 9, 5, 8], [4,5,6,7, 9], [8, 9, 10, 11, 12]], 3),
        [[1, 1, 1], [2, 2, 3], [4, 5, 5]])
        self.assertEqual(min_matrix([[3, 2, 1, 4, 6], [5, 2, 6, 3, 7], [5, 8, 9, 5, 8], [4,5,6,7, 9], [8, 9, 10, 11, 12]], 2),
        [[2, 1, 1, 3], [2, 2, 3, 3], [4, 5, 5, 5], [4, 5, 6, 7]])

    def test_max_window(self):
        self.assertEqual(max_window([3, 2, 1, 4, 5, 2, 6, 3, 5], 3), [3, 4, 5, 5, 6, 6, 6])
        self.assertEqual(max_window([3, 2, 1, 4, 5], 2), [3, 2, 4, 5])
        self.assertEqual(max_window([2, 2, 5, 4], 2), [2, 5, 5])
        self.assertEqual(max_window([1, 2, 3, 4, 5, 6, 7], 3), [3, 4, 5, 6, 7])
        self.assertEqual(max_window([7, 5, 4, 3, 6, 5, 2, 5, 4, 1], 3), [7, 5, 6, 6, 6, 5, 5, 5])


if __name__ == "__main__":
    unittest.main()