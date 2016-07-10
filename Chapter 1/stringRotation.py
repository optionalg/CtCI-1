import unittest

def isSubstring(s,sub):
	return sub in s

def stringRotation(s1,s2):
	if len(s1) == len(s2) != 0:
		return isSubstring(s1 + s1, s2)
	return False


class Test(unittest.TestCase):
	def test(self):
		self.assertTrue(stringRotation('erbottlewat','waterbottle'))
		self.assertFalse(stringRotation('watermelon','mewaterlon'))
		self.assertTrue(stringRotation('watermelon','melonwater'))
		self.assertTrue(stringRotation('melonwater','watermelon'))

if __name__ == "__main__":
	unittest.main()