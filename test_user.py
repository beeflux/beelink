import unittest
from user import UserProfile

class TestUserProfile(unittest.TestCase):

	def setUp(self):
		self.userprofile = UserProfile('neha','21','01')

	def test_create_profile(self):
		self.userprofile.create_profile("hello this is neha")
		self.assertEqual(self.userprofile.info,"hello this is neha")

if __name__=="__main__":
	unittest.main()    

   

