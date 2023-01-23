five_integer = int(input("Enter any five integer digits: "))
if five_integer > 9999 and five_integer < 100000:
	num_1 = five_integer//10000
	num_2 = five_integer//1000%10
	num_3 = five_integer//100%100%10
	num_4 = five_integer%100//10
	num_5 = five_integer%10

	print(num_1,"   ",num_2,"   ",num_3,"   ",num_4,"   ",num_5)
else:
	print("You were asked to enter five integers")
print()
num = 1
while num <= 10:
	print(num)
	num += 1
print()
grocery_list = ["rice","beans","yam","plantain","meat"]
for food in grocery_list:
	print("i want to eat",food) 
print()
num = 1
for num in range(10):
	print(num)

numbers = [1,2,3,4,5]
for number in numbers:
	if number == 3:
		print("found")
		print(number)
		break