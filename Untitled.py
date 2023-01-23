# Target Heart ❤ rate and Maximun Heart ❤ rate calculator
# Maximum Heart rate = 220 - age(in years)
# Target Heart rate is between 50% - 85% of maximum depending on gender, age, health or fitness level


# import the date time function from the date time module to get the current date
# Display Welcome
# Prompt the user to enter his or her fitness level
# match

# case beginner
# Prompt the user to enter his or her year of birth
# declare variable current year and initialize it to the current year
# subtract the users year of birth from the current year to get the user's age
# declare variable maximum heart rate
# assign 220 minus the users age to the maximum heart rate variable
# declare variable Target heart rate
# initialize it to be 60% of maximum heart rate
# print out the maximum heart rate and the units in beats per minute (bpm)
# print out the target heart rate and the units in beats per minute (bpm)

# case intermediate
# Prompt the user to enter his or her year of birth
# declare variable current year and initialize it to the current year
# subtract the users year of birth from the current year to get the user's age
# declare variable maximum heart rate
# assign 220 minus the users age to the maximum heart rate variable
# declare variable Target heart rate
# initialize it to be 70% of maximum heart rate
# print out the maximum heart rate and the units in beats per minute (bpm)
# print out the target heart rate and the units in beats per minute (bpm)

# case veryfit
# Prompt the user to enter his or her year of birth
# declare variable current year and initialize it to the current year
# subtract the users year of birth from the current year to get the user's age
# declare variable maximum heart rate
# assign 220 minus the users age to the maximum heart rate variable
# declare variable Target heart rate
# initialize it to be 85% of maximum heart rate
# print out the maximum heart rate and the units in beats per minute (bpm)
# print out the target heart rate and the units in beats per minute (bpm)


from datetime import datetime, date

print("Welcome")
name = input("Please enter your name: ").lower()
fitness_level = input("{name} Please enter you fitness level: ".format(name=name)).lower()
match fitness_level:
    case "beginner":
        now = datetime.now()
        users_year_of_birth = input("Please enter your birth date in the format DD-MM-YYYY: ")
        birth_date = datetime.strptime(users_year_of_birth, "%d-%m-%Y").date()
        current_year = now.year
        users_age = current_year - birth_date.year
        maximum_heart_rate = 220 - users_age
        target_heart_rate = (60 / 100) * maximum_heart_rate
        print("{} your maximum heart rate is: {} bpm".format(name, maximum_heart_rate))
        print(f"and your target heart rate is: {target_heart_rate}bpm")
    case "intermediate":
        now = datetime.now()
        users_date_of_birth = input("Please enter your birth date in the format DD-MM-YY: ")
        birth_date = datetime.strptime(users_year_of_birth, "%d-%m-%Y").date()
        current_year = now.year
        users_age = current_year - birth_date.year
        maximum_heart_rate = 220 - users_age
        target_heart_rate = (70 / 100) * maximum_heart_rate
        print("{} your maximum heart rate is: {} bpm".format(name, maximum_heart_rate))
        print(f"and your target heart rate is: {target_heart_rate}bpm")
    case "veryfit":
        users_year_of_birth = int(input("{0} please enter your year of birth: ".format(name)))
        current_year = 2023
        users_age = current_year - users_year_of_birth
        maximum_heart_rate = 220 - users_age
        target_heart_rate = (85 / 100) * maximum_heart_rate
        print("{} your maximum heart rate is: {} bpm".format(name, maximum_heart_rate))
        print(f"and your target heart rate is: {target_heart_rate}bpm")

# int(input("{0} please enter your year of birth: ".format(name)))