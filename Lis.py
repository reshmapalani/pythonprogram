try:
	list1=[3,4,5,6]
	print(list1[2])
	raise NameError
except:
	print("index is out of range")
else:
	print("successfully executed")
finally:
	print("completed")			