# words = "I am Michael"
#for word in words:
#	print(word)

start_prompt = int(input("Enter 1 to start: "))
#input = int(start_prompt)
if start_prompt == 1:
	question1 = input("Does a monkey have two tails(yes/no): ").lower()
	if question1 == "no":
		print("You are correct a monkey has only one tail")
	elif question1 == "yes":
		print("You are wrong, a monkey has one tail")
	else:
		print("Please enter a yes or no")
	question2 = input("Is human a mammal(yes/no): ").lower()
	if question2 == "yes":
		print("You are correct, Human are classified as a mammal") 
	elif question2 == "no":
		print("You are wrong, Humans are classified as a mammal")
	else:
		print("Please enter a yes or no")
else:
	print("You were asked to enter 1 to start")  	

