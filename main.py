# Base Payrate Calculator
class basepay:
    # payrate = float(input("What is your current payrate? $"))
    # work_week = float(input("How many hours are in typical pay period? "))
    # hours_worked = float(input("How many hours did you work during your pay period? "))
    # ot_multiplier = float(input("How much does your payrate multiply by with overtime? "))
    payrate = 20
    work_week = 40
    ot_multiplier = 2
    hours_worked = 50
    if hours_worked > work_week:
        ot_hours = hours_worked - work_week
    else:
        ot_hours = 0
    print("You work", int(ot_hours), "hours of overtime this pay period!")
    reg_basepay = (hours_worked - ot_hours) * payrate
    ot_basepay = ot_hours * payrate * ot_multiplier
    basepay_total = reg_basepay + ot_basepay
    print("Your basepay for this pay period will be: $", basepay_total)


class differential:
    diff_exist = float(input("Does your job offer shift differentials? 1 = yes | 2 = no "))
    