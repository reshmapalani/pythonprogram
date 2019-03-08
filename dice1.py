from random import randint
doubles = 0
num1 = randint(1, 6)
num2 = randint(1, 6)
print ("Do you want to roll? yes or no")
answer = raw_input()
while answer.lower()[0] == "y":
    print ("ou rolled a", num1, "and a", num2, ". Your total is",num1 + num2)
    while num1 == num2:
        
    print ("Roll again? Yes or no")
    answer = raw_input()
print "Okay. YOu rolled", doubles, "doulbes."                         