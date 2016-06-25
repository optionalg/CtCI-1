import unittest

def isUnique(testString):
	chars = set()
	for let in testString:
		if let in chars:
			return False
		else:
			chars.add(let)
	return True

def isUniqueBitVect(testString):
	checker = 0
	for let in testString:
		val = ord(let) - ord('a')
		if(checker & (1 << val) > 0):
			return False
		checker |= (1 << val)
	return True

class Test(unittest.TestCase):
	def test(self):
		self.assertTrue(isUnique('abcdefg'))
		self.assertFalse(isUnique('abcdeffg'))
	def testBit(self):
		self.assertTrue(isUniqueBitVect('abcdefg'))
		self.assertFalse(isUniqueBitVect('abcdeffg'))

if __name__ == "__main__":
	unittest.main()