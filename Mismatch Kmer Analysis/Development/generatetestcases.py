import random
testcases=[]

for i in range(7):
	z=random.randrange(0,(len(string)-500))
	testcases.append(string[z:z+501])
	
filename = open("testcases.txt", "wt")

for i in testcases:
	filename.write(i)
	filename.write("\n")


filename.close()