def funcl():
	print("hii")
	print("hello")
funcl()	

#with parameters
def func2(a):#a=1
 	print("hii\t",a)
func2("abs")

#with 2|3parameters
def func3(a,b,c):#a=2,b=5,c=6
    d=a+b+c
    print(a,b,c,d)
func3(2,5,6)

#with default parameter
def func4(university="CMR"):
 	print("i am in" + "\t"+ university)
func4("IIM")
func4("IIT")
func4() 

#return statement
def func7(a,b,c):#a=2,b=5,c=6
 	d=a+b+c
 	return d
e=func7(2,5,6)
print(e)

#calling one func from other and return statement
def func5(a,b):
 	print("hey other function")
 	c=a+b
 	return c
def func6():
 	print("hello,i am gonna call other function")
 	s=func5(2,7)
 	print("addition is",s)
func6() 	  	  	 		                  	                
