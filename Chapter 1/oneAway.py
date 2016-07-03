import unittest

def oneAway(s1,s2):
	if len(s1) == len(s2):
		return oneReplace(s1,s2)
	elif len(s1) + 1 == len(s2):
		return oneInsert(s1,s2)
	elif len(s1) - 1 == len(s2):
		return oneInsert(s2,s1)
	else:
		return False

def oneReplace(s1,s2):
	dif = 0
	for c1, c2 in zip(s1,s2):
		if c1 != c2:
			dif += 1
	return dif <= 1

def oneInsert(s1,s2):
	dif = False
	x, y = 0 , 0
	while x < len(s1) and y < len(s2):
		if s1[x] != s2[y]:
			if dif:
				return False
			dif = True
			x += 1
		x += 1
		y += 1
	return True


class Test(unittest.TestCase):
	def test(self):
		self.assertTrue(oneAway('pale','ple'))
		self.assertTrue(oneAway('ple','pale'))
		self.assertTrue(oneAway('pales','pale'))
		self.assertTrue(oneAway('pale','bale'))
		self.assertFalse(oneAway('pale','ble'))

if __name__ == "__main__":
	unittest.main()