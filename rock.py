import random
l=['r','p','s']
d={'r':"rock",'p':"paper",'s':"scissor"}
us=0
cs=0
while True:
	i=input("enter ur choice:")
	if i in d:
		print("user chooses",d[i])
	c=random.choice(l)
	if c in d:
		print("computer chosses",d[c])
	if i=='n':
		exit()
	elif i == c:
		print("tie")
	elif i=='r' and c=='s':
		us=us+1
		print("user has won",us)
	elif i=='p' and c=='r':
		us=us+1
		print("user wins",us)
	elif i=='s' and c=='p':
		us=us+1
		print("user wins",us)
	elif i=='r' and c=='p':
		cs=cs+1
		print("computer has won",cs)
	elif i=='p'	and c=='s':
		cs=cs+1
		print("computer wins",cs)
	elif i=='s'	and c=='r':
		cs=cs+1
		print("computer wins",cs)