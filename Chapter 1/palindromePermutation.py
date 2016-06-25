import unittest

def palinPerm(s):
	s = s.replace(' ','').lower()
	count = {}

	for let in s:
		if let in count:
			count[let] += 1
		else:
			count[let] = 1

	oddCount = 0
	for x in count:
		if count[x] % 2 == 1:
			oddCount += 1

	return oddCount < 2

class Test(unittest.TestCase):
	def test(self):
		self.assertTrue(palinPerm('Tact Coa'))
		self.assertTrue(palinPerm('Able was I ere I saw Elba'))
		self.assertFalse(palinPerm('So patient a nurse to nurse a patient so'))
		self.assertFalse(palinPerm('Random Words'))

if __name__ == "__main__":
	unittest.main()