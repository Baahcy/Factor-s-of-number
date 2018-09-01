
print ("This program is to find the factors of a number")
print ("--+" * 3)


number = int(input("Enter a number : "))

for a in range(1 , number + 1):
	if number % a == 0:
		print (a)

print ("--+" * 3)
