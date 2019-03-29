import matplotlib.pyplot as plt
import csv
	# csv file name
filename="a3text.csv"
#initializing the titles amd rows list
x=[]
y=[]
# reading csv file
with open(filename,'r') as csvfile:
	# creating a csv reader object
	csvreader = csv.reader(csvfile)

	# extracting fields names through first row
	# fields = csvreader.next()


	# extracting each data row one by one
	for row in csvreader:
		x.append(row[0])
		y.append(row[1])
print(x)
print(y)
plt.plot(x,y)
plt.show()
	# get total number of rows.
					