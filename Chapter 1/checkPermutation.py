import unittest

def clean(s):
	return s.replace(' ','').lower()


def checkPermutation(s1,s2):
	s1 = clean(s1)
	s2 = clean(s2)
	
	if len(s1) != len(s2):
		return False

	count = {}

	for let in s1:
		if let in count:
			count[let] += 1
		else:
			count[let] = 1

	for let in s2:
		if let in count:
			count[let] -= 1
		else:
			count[let] = 1

	for x in count:
		if count[x] != 0:
			return False

	return True
	
def checkPermutationSort(s1,s2):
	s1 = clean(s1)
	s2 = clean(s2)

	return sorted(s1) == sorted(s2)


class Test(unittest.TestCase):
	def testDict(self):
		self.assertTrue(checkPermutation('dog','god'))
		self.assertTrue(checkPermutation('Clint Eastwood','old west action'))
		self.assertFalse(checkPermutation('do','god'))
	def testSort(self):
		self.assertTrue(checkPermutationSort('dog','god'))
		self.assertTrue(checkPermutationSort('Clint Eastwood','old west action'))
		self.assertFalse(checkPermutationSort('do','god'))


if __name__ == "__main__":
	unittest.main()