int_1 = int(input("Enter the first integer: "))
int_2 = int(input("Enter the second integer: "))
int_3 = int(input("Enter the third integer: "))

sum = int_1 + int_2 + int_3

product = int_1 * int_2 * int_3

average = (int_1 + int_2 + int_3)/3

print("The sum of the three integers is: ",sum)
print("The product of the three integers is: ",product)
print("The average of the three integers is: ",average)

if int_1 > int_2 and int_1 > int_3:
	print(int_1, " is the largest")
elif int_2 > int_1 and int_2 > int_3:
	print(int_2, " is the largest")
elif int_3 > int_1 and int_3 > int_2:
	print(int_3, " is the largest")

if int_1 < int_2 and int_1 < int_3:
	print(int_1, " is the smallest")
elif int_2 < int_1 and int_2 < int_3:
	print(int_2, " is the smallest")
elif int_3 < int_1 and int_3 < int_2:
	print(int_3, " is the smallest")