import unittest

def urlify(s,l):
	newIndex = len(s)
	s = list(s)

	for x in reversed(range(l)):
		if s[x] == ' ':
			s[newIndex - 3:newIndex] = '%20'
			newIndex -= 3
		else:
			s[newIndex - 1] = s[x]
			newIndex -= 1
	return ''.join(s)

class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(urlify('Mr John Smith    ', 13), 'Mr%20John%20Smith')
		self.assertEqual(urlify('much ado about nothing      ', 22), 'much%20ado%20about%20nothing')		

if __name__ == "__main__":
	unittest.main()