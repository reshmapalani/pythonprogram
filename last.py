class test:
	h=0
	def my_fun(self,k):
		print("hii,i am in a class")
		self.h=k
		print(self.h)
o=test()
o1=test()
o.my_fun(2)
o1.my_fun(4)
o3=test()
print(o3.h)	