import unittest

def urlify(s,l):
#fix, doesn't work
	newIndex = len(s)

	for x in reversed(range(l)):
		if s[x] == ' ':
			s[newIndex - 3:newIndex] = '%20'
			newIndex -= 3
		else:
			s[newIndex - 1] = s[x]
			newIndex -= 1
	return s

class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(urlify('Mr John Smith    ', 13), 'Mr%20John%20Smith')

if __name__ == "__main__":
	unittest.main()