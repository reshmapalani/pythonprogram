try:
	a=int(input("enter the number"))
	if a<3:
		b=int(a/(a-3))
	elif a==3:
		raise ZeroDivisionError
 	elif a>3:
 		raise NameError 	
except ZeroDivisionError:
	print("some error occured")
except NameError:
	print("u have choosen a number greater than 3")
else:
	print(b)


