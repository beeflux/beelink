class Company:

	def __init__(self,company_name):
		self.company_name = company_name

	def print_company(self):
		return self.company_name
	

class Company_profile(Company):
	
	def __init__(self,company_name,faculty):
		super().__init__(company_name)
		self.faculty = faculty
	
	def posts(self,likes,comments):
		self.likes = likes
		self.comment = comments
		
	def information(self,title,postedby):
		self.title = title
		self.postedby = postedby

	def print_profile(self):
		print(self.company_name + " " + self.faculty + " have got " + self.likes + " likes " + self.comment + " comment in the post titled " + self.title)

x = Company('Beeflux')
x.print_company()
y = Company_profile('Beeflux', 'IT company')
y.posts('20','2')
y.information('python workshop','Harish')
y.print_profile()




