import gross


class fedpay:
    annual_gross_pay = gross.gross_pay * gross.basepay.pay_periods
    filing_status = float(input("What is your federal tax filing status? 1 = single | 2 = "))
    if filing_status == 1:
        # Tax filing status is single
        if annual_gross_pay <= 10275:
            net_pay = annual_gross_pay * 0.9
        elif 10275 < annual_gross_pay <= 41775:
            net_pay = annual_gross_pay - (((annual_gross_pay - 10275) * 0.12) + 1027.50)
        elif 41775 < annual_gross_pay <= 89075:
            net_pay = annual_gross_pay - (((annual_gross_pay - 41775) * 0.22) + 4807.50)
        elif 89075 < annual_gross_pay <= 170050:
            net_pay = annual_gross_pay - (((annual_gross_pay - 89075) * 0.24) + 15213.50)
        elif 170050 < annual_gross_pay <= 215950:
            net_pay = annual_gross_pay - (((annual_gross_pay - 170050) * 0.32) + 34647.50)
        elif 215950 < annual_gross_pay <= 539900:
            net_pay = annual_gross_pay - (((annual_gross_pay - 215950) * 0.35) + 49335.50)
        elif 539900 < annual_gross_pay:
            net_pay = annual_gross_pay - (((annual_gross_pay - 539900) * 0.37) + 162718)
        else:
            net_pay = "undefined"
