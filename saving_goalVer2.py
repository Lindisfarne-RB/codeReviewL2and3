def validate_float(prompt):
    while True:
        try:
            float_input = float(input(prompt))
            return float_input
        except:
            print("Please input an integer")



input_saving_goal = True
while input_saving_goal:

#input saving goal and calculating weekly salary

# input salary type and calculating weekly income
    while True:
        try:
            saving_goal = int(input("Enter your saving goal"))
            break
        except:
            print("Please input a number")
        type_of_income = ""
        while type_of_income not in ["hourly" , "annual"]:
            type_of_income = input(
                """Do you have hourly wage or annual salary?
                                    Please input 'hourly' or 'annual'. """)

        if type_of_income == "hourly":
            while True:
                try:
                    hours_per_week = float(input("How many hours do you work per week?"))
                    break
                except:
                    print("input a number")

            while True:
                try:
                    hourly_wage = float(input("What is your hourly wage?"))
                    break
                except:
                    print("input a number")

            weekly_income = hours_per_week * hourly_wage


        if type_of_income == "salary":
           #write code to calculate weekly income if you have annual salary

#ask the user to run the program again
    use_again = input("Do you wish to use this program again Press Y or N")
    if use_again == 'Y':
        input_saving_goal = True
    else:
        print("Thank you for using my program")
        input_saving_goal = False

