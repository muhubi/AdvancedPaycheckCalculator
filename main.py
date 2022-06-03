import gross
import fed

print(" ")
print("-------------------------")
print(" ")
print("Your basepay for this pay period will be: $", gross.basepay.reg_basepay)
print("You work", int(gross.basepay.ot_hours), "hours of overtime this pay period!")
print("Your OT pay for this pay period will be: $", gross.basepay.ot_basepay)
print("Your weekend pay differential will be: $", gross.differential.weekend_pay)
print("Your evening pay differential will be: $", gross.differential.evening_pay)
print("Your overnight pay differential will be: $", gross.differential.overnight_pay)
print(" ")
print("Your total gross pay for this pay period will be: $", gross.gross_pay)
print("Your total federal tax deduction = $", gross.gross_pay - (fed.fedpay.net_pay / gross.basepay.pay_periods))
print("Your total net pay for this pay period is: $", fed.fedpay.net_pay / gross.basepay.pay_periods)