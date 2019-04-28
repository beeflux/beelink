import unittest
from company import Company, Company_profile

class Test_Company(unittest.TestCase):
	def setUp(self):
		self.company_name=Company_Profile('Beeflux', 'IT company')
		self.assertTrue(len.company_name != text)
	
if __name__ == '__main__':
    unittest.main()
