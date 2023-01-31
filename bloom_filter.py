# Python 3 program to build Bloom Filter
# Install mmh3 and bitarray 3rd party module first
# pip install mmh3
# pip install bitarray
import math
import mmh3
from bitarray import bitarray
from wordleft import valid_word_list

class BloomFilter(object):

	'''
	Class for Bloom filter, using murmur3 hash function
	'''

	def __init__(self, items_count, fp_prob):
		'''
		items_count : int
			Number of items expected to be stored in bloom filter
		fp_prob : float
			False Positive probability in decimal
		'''
		# False possible probability in decimal
		self.fp_prob = fp_prob

		# Size of bit array to use
		self.size = self.get_size(items_count, fp_prob)

		# number of hash functions to use
		self.hash_count = self.get_hash_count(self.size, items_count)

		# Bit array of given size
		self.bit_array = bitarray(self.size)

		# initialize all bits as 0
		self.bit_array.setall(0)

	def add(self, item):
		'''
		Add an item in the filter
		'''
		digests = []
		for i in range(self.hash_count):

			# create digest for given item.
			# i work as seed to mmh3.hash() function
			# With different seed, digest created is different
			digest = mmh3.hash(item, i) % self.size
			digests.append(digest)

			# set the bit True in bit_array
			self.bit_array[digest] = True

	def check(self, item):
		'''
		Check for existence of an item in filter
		'''
		for i in range(self.hash_count):
			digest = mmh3.hash(item, i) % self.size
			if self.bit_array[digest] == False:

				# if any of bit is False then,its not present
				# in filter
				# else there is probability that it exist
				return False
		return True

	@classmethod
	def get_size(self, n, p):
		'''
		Return the size of bit array(m) to used using
		following formula
		m = -(n * lg(p)) / (lg(2)^2)
		n : int
			number of items expected to be stored in filter
		p : float
			False Positive probability in decimal
		'''
		m = -(n * math.log(p))/(math.log(2)**2)
		return int(m)

	@classmethod
	def get_hash_count(self, m, n):
		'''
		Return the hash function(k) to be used using
		following formula
		k = (m/n) * lg(2)

		m : int
			size of bit array
		n : int
			number of items expected to be stored in filter
		'''
		k = (m/n) * math.log(2)
		return int(k)

import unittest
import time

class FloydTest(unittest.TestCase):
    def test_bloom_speed(self):
        print(f"Number of words: {len(valid_word_list)}")

        my_dict = {}
        start_time = time.time()
        for word in valid_word_list:
            if not my_dict.get(word):
                my_dict[word] = True
        print(f"dictionary lookup took: {time.time() - start_time}")

        my_bloom = BloomFilter(len(valid_word_list), .05)
        start_time = time.time()
        num_stored = 0
        for word in valid_word_list:
            if not my_bloom.check(word):
                my_bloom.add(word)
                num_stored+=1

        print(f"bloom lookup took: {time.time() - start_time}")
        print(f"bloom stored {num_stored} in {my_bloom.size}")


if __name__ == "__main__":
    unittest.main()