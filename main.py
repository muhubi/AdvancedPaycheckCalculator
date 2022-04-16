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
    weekend_hours_worked = 8
    evening_hours_worked = 8
    overnight_hours_worked = 10
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
    if diff_exist == 1:
        diff_weekend = float(input("What kind of differential is your weekend pay? 1 = increase hourly pay? | 2 ="
                                   " pay multiplier | 3 = no weekend differential "))
        if diff_weekend == 1:
            diff_weekend_payrate = float(input("How much extra is your hourly rate? "))
        elif diff_weekend == 2:
            diff_weekend_paymulti = float(input("What is your pay multiplier? "))
        else:
            print("No Weekend Differential added to pay period.")
        diff_evening = float(input("What kind of differential is your evening pay? 1 = increase hourly pay? | 2 ="
                                   " pay multiplier | 3 = no evening differential "))
        if diff_evening == 1:
            diff_evening_payrate = float(input("How much extra is your hourly rate? "))
        elif diff_evening == 2:
            diff_evening_paymulti = float(input("What is your pay multiplier? "))
        else:
            print("No Evening Differential added to pay period.")
        diff_overnight = float(input("What kind of differential is your overnight pay? 1 = increase hourly pay? | 2 ="
                                     " pay multiplier | 3 = no overnight differential "))
        if diff_overnight == 1:
            diff_overnight_payrate = float(input("How much extra is your hourly rate? "))
        elif diff_overnight == 2:
            diff_overnight_paymulti = float(input("What is your pay multiplier? "))
        else:
            print("No Overnight Differential added to pay period.")
