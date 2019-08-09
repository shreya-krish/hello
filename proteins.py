f = open("proteins", "r")
x = f.readlines()

for i in (x):
	for j in range(0,len(i)-1):
		if i[j]== ">":
			print(i)
