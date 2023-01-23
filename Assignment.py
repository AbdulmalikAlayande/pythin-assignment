"""words = "I am Michael"
for word in words:
	print(word)
woor = words.split()
for word in woor:
	print(word)
for i in range(0,5,i*2):
	print(i)

Prompt the user to start
if the user enters 1
typecast the users response to string
declare variable counter and initialize it to 0
while counter is not equal to 0
if the users respone is 1
import random
then declare variable questions and use the........
using match case if the random question generated is question one ask the question and display the answer
prompt the user to enter their answer
using match case if the random question generated is question two ask the question and display the answer
prompt the user to enter their answer
using match case if the random question generated is question three ask the question and display the answer
prompt the user to enter their answer
using match case if the random question generated is question four ask the question and display the answer
prompt the user to enter their answer
using match case if the random question generated is question five ask the question and display the answer
prompt the user to enter their answer
using match case if the random question generated is question six ask the question and display the answer
prompt the user to enter their answer
using match case if the random question generated is question seven ask the question and display the answer
prompt the user to enter their answer
using match case if the random question generated is question eight ask the question and display the answer
prompt the user to enter their answer
then increment counter.
"""
import random

start_prompt = int(input("Enter 1 to start (0 to end): "))
input_start = int(start_prompt)
counter = 1
while counter != 0:
	if start_prompt == 1:

		questions =["question_one",
			"question_two",
			"question_three",
			"question_four",
			"question_five",
			"question_six",
			"question_seven",
			"question_eight"]
		random_questions = random.choice(questions)

		match random_questions:
			case "question_one":
				question1 = input("Does a monkey have two tails(yes/no): ").lower()
				if question1 == "no":
					print("You are right, a monkey has one tail")
				elif question1 == "yes":
					print("You are wrong, a monkey has one tail")
				else:
					print("Please enter a yes or no")
				print()

			case "question_two":
				question2 = input("Is human a mammal(yes/no): ").lower()
				if question2 == "yes":
					print("You are correct, Human are classified as a mammal") 
				elif question2 == "no":
					print("You are wrong, Humans are classified as a mammal")
				else:
					print("Please enter a yes or no")
				print()

			case "question_three":
				question3 = input("who was the first prime minister of Nigeria: ").lower()
				if question3 == "abubakar tafawa balewa":
					print("Correct, Abubakar Tafawa Balewa is the first prime minister of Nigeria")
				else: 
					print("You are wrong, the first prime minister is Abubakar Tafawa Balewa")
				print()

			case "question_four":
				question4 = (input("When was police force established in Nigeria(a.1930, b.1959, c.1963, d.1914): ")).lower()
				if question4 == 'a':
					print("Correct, The police force was enstablished in 1930 by Louis Edet")
				elif question4 == 'b':
					print("Wrong, The police force was enstablished in 1930 by Louis Edet")
				elif question4 == 'c':
					print("Wrong, The police force was enstablished in 1930 by Louis Edet")
				else:
					print("Wrong")
				print()

			case "question_five":
				question5 = input("Which metal is the most elastic: ").lower()
				if question5 == "steel":
					print("Correct, Steel is considered the most elastic because it regains it original form after removing the effect of an external force")
				else:
					print("wrong")
				print()

			case "question_six":
				question6 = input("______ & ______ logical operators do not perform short circuit(a.| and &, b.|| and &&, c.! and ||, d.| and ^)").lower()
				if question6 == "a":
					print("Correct, The boolean logical inclusive OR and the boolean logical and do not perform short circuit")
				elif question6 == "b":
					print("Wrong")
				elif question6 == "c":
					print("Wrong")
				else:
					print("Wrong")
				print()

			case "question_seven":
				question7 = input("Is python an OOP language or a Procedural Programming language").lower()
				if question7 == "oop":
					print("Correct, Python is an Object Oriented Programming Language")
				elif question7 == "procedural programming language":
					print("Wrong, Python is an Object Oriented Programming Language")
				else:
					print("Wrong")
				print()

			case "question_eight":
				question8 = input("What is the associativity of an assignment operator: ").lower()
				if question8 == "right to left":
					print("Correct, The assignment operator associates from right to left")
				elif question8 == "left to right":
					print("Wrong, The assignment operator associates from right to left")
				else:
					print('I will report you to Chibuzo')
				print()

	counter += 1
else:
	print("You were asked to enter 1 to start")  	

