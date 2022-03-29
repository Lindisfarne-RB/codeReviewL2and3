input_saving_goal = True
while input_saving_goal:

#input saving goal and calculating weekly salary
    saving_goal = int(input("Enter your saving goal"))
    salary_type = input("Enter your salary type - Press s for salaried or press h for hourly wages")
#input salary type and calculating weekly income
    if salary_type == 's':
        salary_annual = int(input("Enter your annual salary"))
        tax_rate = int(input("Enter your tax percentage"))
        net_salary = salary_annual - (salary_annual * tax_rate /100)
        weekly_income = net_salary / 52
    elif salary_type == 'h':
        hours_worked = int(input("How many hours do you work in a week"))
        hour_charges = int(input("How many $ per hour"))
        weekly_income = hour_charges * hours_worked
    else:
        print("Incorrect input ")
    weekly_expenses = int(input("Enter weekly expenses"))
    saving_weekly = weekly_income - weekly_expenses
#ask the user to run the program again
    use_again = input("Do you wish to use this program again Press Y or N")
    if use_again == 'Y':
        input_saving_goal = True
    else:
        print("Thank you for using my program")
        input_saving_goal = False

