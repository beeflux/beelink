class User:

	def __init__(self,name,age):
		 self.name = name
		 self.age = age


class UserProfile(User):

	def __init__(self,name,age,u_id):
		super().__init__(name,age)

		self.u_id = u_id

	def create_profile(self,info):
		self.info=info


	def print_information(self):
		print(self.name+" "+"is"+self.age+" "+"years old "+" "+" has user id"+" "+self.u_id+" "+ "and has the info"+" "+ self.info)



x=User('neha',21)
y=UserProfile('neha','21','01')
y.create_profile("hello this is neha")
y.print_information()

