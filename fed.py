import gross

class fedpay:
    annual_gross_pay = gross.gross_pay * gross.basepay.pay_periods
    filing_status = float(input("What is your federal tax filing status? 1 = single | 2 = "))
    if filing_status == 1:
        # Tax filing status is single
        if annual_gross_pay <= 10275:
            net_pay = annual_gross_pay * 0.9
        elif 10276 <= annual_gross_pay <= 41775:
            net_pay = annual_gross_pay - (((annual_gross_pay - 10275) * 0.12) + 1027.50)
        elif 41776 <= annual_gross_pay <= 89075:
            net_pay = annual_gross_pay - (((annual_gross_pay - 41775) * 0.22) + 4807.50)
        else:
            net_pay = "undefined"