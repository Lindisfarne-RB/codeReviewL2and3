#fully working code

import math
def validate_float(prompt):
    while True:
        try:
            float_input = float(input(prompt))
            return float_input
        except ValueError:
            print("Please input a floating point number ")


def validate_text_input(prompt,options):
    print(options)
    while True:
        try:
            text_input = input(prompt)
            return text_input
        except TypeError:
            print("Please enter text")

def get_weekly_expenses():
    expenses_list = ["rent" , "food" , "social","other" ]
    total_expense_cost = 0.0
    for expense in range(len(expenses_list)):
        total_expense_cost += validate_float("How much do you spend on {}".format(expenses_list[expense]))
    return total_expense_cost

def get_weekly_income():
    type_of_income = ""
    while type_of_income not in ["hourly", "annual"]:
        type_of_income = validate_text_input(
            """Do you have hourly wage or annual salary?
                                Please input 'hourly' or 'annual'. """, ["hourly", "annual"])
        if type_of_income == "hourly":
            while True:
                try:
                    hours_per_week = float(input("How many hours do you work per week?"))
                    if hours_per_week > 0:
                        break
                except ValueError:
                    print("input a number")
            while True:
                try:
                    hourly_wage = float(input("What is your hourly wage?"))
                    if hourly_wage > 0:
                        break
                except ValueError:
                    print("input a number")
            weekly_income = hours_per_week * hourly_wage
            print("Weekly income =", weekly_income)


        elif type_of_income == "annual":
            # write code to calculate weekly income if you have annual salary

            annual_salary = validate_float("What is your annual salary?")
            if annual_salary > 0:
                weekly_income = annual_salary / 52

        else:
            pass

    return weekly_income


def display_savings_report(saving_goal,weekly_savings,weeks_to_goal):
    if weekly_savings > 0:
        weeks_to_goal = saving_goal / weekly_savings
        print("Thank you for using saving calculator")
        print("Your saving goal is $ {}".format(saving_goal))
        print("You save $ {}".format(weekly_savings))
        print("It will take {} weeks for you to save for your goal".format(round(weeks_to_goal)))

def calculate_weeks_goal(saving_goal , weekly_saving):
    Numweeks =  saving_goal /weekly_saving
    #I would like to round my weeks  Numweeks = round(Numweeks)
    print("Weeks needed to save for goal", Numweeks)


    return Numweeks

def calculate_income_after_tax(weekly_income):
    tax_rate = float(input("What is your tax rate"))
    tax_multiplier = (100 - tax_rate) / 100
    income_after_tax = weekly_income * tax_multiplier
    return income_after_tax

def calculate_weekly_saving():
    weekly_income = get_weekly_income()
    weekly_income_after_tax = calculate_income_after_tax(weekly_income)
    weekly_expenses = get_weekly_expenses()
    weekly_saving = weekly_income_after_tax - weekly_expenses
    return weekly_saving

def is_user_calculating():
    use_again = input("Do you wish to use this program again Press Y or N")
    if use_again == 'Y' or use_again == 'y':
        return True
    else:
        print("Thank you for using my program")

        return  False





def main():
    print("-----------------I am in main----------------------")
    print(input_saving_goal)
    while is_user_calculating():
        saving_goal = validate_float("Pls enter your saving goal")
        weekly_saving = calculate_weekly_saving()
        weeks_to_goal = calculate_weeks_goal(saving_goal,weekly_saving)
        display_savings_report(saving_goal,weekly_saving,weeks_to_goal)
    print("bye")


input_saving_goal = True
main()
