import random
d = {8:37,38:9,11:2,13:34,40:68,65:46,52:81}

p = random.choice([2,8,9,13,40,65,52])

print("You got",p)

if p in d:
	print("You can go to ",d[p])