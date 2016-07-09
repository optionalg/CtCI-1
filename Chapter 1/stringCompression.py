import unittest

def stringCompression(string):
	compressed = []
	counter = 0

	for x in range(len(string)):
		if x != 0 and string[x] != string[x-1]:
			compressed.append(string[x-1] + str(counter))
			counter = 0
		counter += 1

	compressed.append(string[-1] + str(counter))

	return min(string, ''.join(compressed), key=len)


class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(stringCompression('aabcccccaaa'),'a2b1c5a3')
		self.assertEqual(stringCompression('abcdef'),'abcdef')		

if __name__ == "__main__":
	unittest.main()