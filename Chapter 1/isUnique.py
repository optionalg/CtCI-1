import unittest

def isUnique(testString):
	chars = set()
	for let in testString:
		if let in chars:
			return False
		else:
			chars.add(let)
	return True

class Test(unittest.TestCase):
	def test(self):
		self.assertTrue(isUnique('abcdefg'))
		self.assertFalse(isUnique('abcdeffg'))

if __name__ == "__main__":
	unittest.main()