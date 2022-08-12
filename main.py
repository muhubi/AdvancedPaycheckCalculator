import gross
import fed

print(" ")
print("-----------------------------------------------------------------------")
print("Your basepay for this pay period will be: $", gross.basepay.reg_basepay)
print(" ")
print("You worked", int(gross.basepay.ot_hours), "hours of overtime this pay period!")
print("Your OT pay for this pay period will be: $", gross.basepay.ot_basepay)
print(" ")
print("Your weekend pay differential will be: $", gross.differential.weekend_pay)
print("Your evening pay differential will be: $", gross.differential.evening_pay)
print("Your overnight pay differential will be: $", gross.differential.overnight_pay)
print(" ")
print("Your total gross pay for this pay period will be: $", gross.gross_pay)

fed_tax_deduction = gross.gross_pay - (fed.fedpay.net_pay / gross.basepay.pay_periods)
total_net_pay = float(fed.fedpay.net_pay / gross.basepay.pay_periods)

print("Your total federal tax deduction = $", float(f'{fed_tax_deduction:.2f}'))
print("Your total net pay for this pay period is: $", float(f'{total_net_pay:.2f}'))
print("-----------------------------------------------------------------------")