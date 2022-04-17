# Base Payrate Calculator
class basepay:
    # payrate = float(input("What is your current payrate? $"))
    # work_week = float(input("How many hours are in typical pay period? "))
    # hours_worked = float(input("How many hours did you work during your pay period? "))
    # ot_multiplier = float(input("How much does your payrate multiply by with overtime? "))
    payrate = 20
    work_week = 40
    hours_worked = 50
    ot_multiplier = 2
    if hours_worked > work_week:
        ot_hours = hours_worked - work_week
    else:
        ot_hours = 0
    reg_basepay = (hours_worked - ot_hours) * payrate
    ot_basepay = ot_hours * payrate * ot_multiplier
    basepay_total = reg_basepay + ot_basepay


# Differential Portion of Calculator
class differential:
    diff_exist = float(input("Does your job offer shift differentials? 1 = yes | 2 = no "))
    if diff_exist == 1:
        # Weekend Diff Section
        weekend_hours_worked = float(input("How many hours of your total hours worked were weekend? "))
        if weekend_hours_worked > 0:
            diff_weekend = float(input("What kind of differential is your weekend pay? 1 = increase hourly pay? | 2 ="
                                       " pay multiplier | 3 = no weekend differential "))
            if diff_weekend == 1:
                diff_weekend_payrate = float(input("How much extra is your hourly rate? "))
                weekend_pay = weekend_hours_worked * (basepay.payrate + diff_weekend_payrate)
            elif diff_weekend == 2:
                diff_weekend_paymulti = float(input("What is your pay multiplier? "))
                weekend_pay = weekend_hours_worked * basepay.payrate * diff_weekend_paymulti
            else:
                diff_weekend_payrate = 0
                diff_weekend_paymulti = 0
                weekend_pay = 0
                print("No Weekend Differential added to pay period.")
        else:
            print("No Weekend Differential added to pay period.")
            diff_weekend_payrate = 0
            diff_weekend_paymulti = 0
            weekend_pay = 0
        # Evening Diff Section
        evening_hours_worked = float(input("How many hours of your total hours worked were evenings? "))
        if evening_hours_worked > 0:
            diff_evening = float(input("What kind of differential is your evening pay? 1 = increase hourly pay? | 2 ="
                                       " pay multiplier | 3 = no evening differential "))
            if diff_evening == 1:
                diff_evening_payrate = float(input("How much extra is your hourly rate? "))
                evening_pay = evening_hours_worked * (basepay.payrate + diff_evening_payrate)
            elif diff_evening == 2:
                diff_evening_paymulti = float(input("What is your pay multiplier? "))
                evening_pay = evening_hours_worked * basepay.payrate * diff_evening_paymulti
            else:
                diff_evening_payrate = 0
                diff_evening_paymulti = 0
                evening_pay = 0
                print("No Evening Differential added to pay period.")
        else:
            print("No Evening Differential added to pay period.")
            diff_evening_payrate = 0
            diff_evening_paymulti = 0
            evening_pay = 0
        # Overnight Diff Section
        overnight_hours_worked = float(input("How many hours of your total hours worked were overnights? "))
        if overnight_hours_worked > 0:
            diff_overnight = float(input("What kind of differential is your overnight pay? 1 = increase hourly pay? |"
                                         " 2 = pay multiplier | 3 = no overnight differential "))
            if diff_overnight == 1:
                diff_overnight_payrate = float(input("How much extra is your hourly rate? "))
                overnight_pay = overnight_hours_worked * (basepay.payrate + diff_overnight_payrate)
            elif diff_overnight == 2:
                diff_overnight_paymulti = float(input("What is your pay multiplier? "))
                overnight_pay = overnight_hours_worked * basepay.payrate * diff_overnight_paymulti
            else:
                diff_overnight_payrate = 0
                diff_overnight_paymulti = 0
                overnight_pay = 0
                print("No Overnight Differential added to pay period.")
        else:
            print("No Overnight Differential added to pay period.")
            diff_overnight_payrate = 0
            diff_overnight_paymulti = 0
            overnight_pay = 0
    else:
        weekend_pay = 0
        evening_pay = 0
        overnight_pay = 0
        print("No Differential added!")


gross_pay = float(basepay.reg_basepay) + float(basepay.ot_basepay) + float(differential.weekend_pay) + \
            float(differential.evening_pay) + float(differential.overnight_pay)
print(" ")
print("-------------------------")
print(" ")
print("Your basepay for this pay period will be: $", basepay.reg_basepay)
print("You work", int(basepay.ot_hours), "hours of overtime this pay period!")
print("Your OT pay for this pay period will be: $", basepay.ot_basepay)
print("Your weekend pay differential will be: $", differential.weekend_pay)
print("Your evening pay differential will be: $", differential.evening_pay)
print("Your overnight pay differential will be: $", differential.overnight_pay)
print(" ")
print("Your total gross pay for this pay period will be: $", gross_pay)