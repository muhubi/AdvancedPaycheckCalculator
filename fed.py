import gross

annual_gross_pay = gross.gross_pay * gross.basepay.pay_periods


class fedbracket:
    filing_status = float(input("What is your federal tax filing status? 1 = Single | 2 = Married, filing jointly | "
                                "3 = Married, filing separately | 4 = Head of Household "))
    if filing_status == 1:
        print("Filing status = Single")
        tax_bracket_1 = 10275
        tax_bracket_2 = 41775
        tax_bracket_3 = 89075
        tax_bracket_4 = 170050
        tax_bracket_5 = 215950
        tax_bracket_6 = 539900
    elif filing_status == 2:
        print("Filing status = Married, filing jointly")
        tax_bracket_1 = 20550
        tax_bracket_2 = 83550
        tax_bracket_3 = 178150
        tax_bracket_4 = 340100
        tax_bracket_5 = 431900
        tax_bracket_6 = 647850
    elif filing_status == 3:
        print("Filing status = Married, filing separately")
        tax_bracket_1 = 10275
        tax_bracket_2 = 41775
        tax_bracket_3 = 89075
        tax_bracket_4 = 170050
        tax_bracket_5 = 215950
        tax_bracket_6 = 323925
    elif filing_status == 4:
        print("Filing status = Head of Household")
        tax_bracket_1 = 14650
        tax_bracket_2 = 55900
        tax_bracket_3 = 89050
        tax_bracket_4 = 170050
        tax_bracket_5 = 215950
        tax_bracket_6 = 539900


class fedpay:
    if annual_gross_pay <= fedbracket.tax_bracket_1:
        net_pay = annual_gross_pay * 0.9
    elif fedbracket.tax_bracket_1 < annual_gross_pay <= fedbracket.tax_bracket_2:
        net_pay = annual_gross_pay - (((annual_gross_pay - fedbracket.tax_bracket_1) * 0.12) + 1027.50)
    elif fedbracket.tax_bracket_2 < annual_gross_pay <= fedbracket.tax_bracket_3:
        net_pay = annual_gross_pay - (((annual_gross_pay - fedbracket.tax_bracket_2) * 0.22) + 4807.50)
    elif fedbracket.tax_bracket_3 < annual_gross_pay <= fedbracket.tax_bracket_4:
        net_pay = annual_gross_pay - (((annual_gross_pay - fedbracket.tax_bracket_3) * 0.24) + 15213.50)
    elif fedbracket.tax_bracket_4 < annual_gross_pay <= fedbracket.tax_bracket_5:
        net_pay = annual_gross_pay - (((annual_gross_pay - fedbracket.tax_bracket_4) * 0.32) + 34647.50)
    elif fedbracket.tax_bracket_5 < annual_gross_pay <= fedbracket.tax_bracket_6:
        net_pay = annual_gross_pay - (((annual_gross_pay - fedbracket.tax_bracket_5) * 0.35) + 49335.50)
    elif fedbracket.tax_bracket_6 < annual_gross_pay:
        net_pay = annual_gross_pay - (((annual_gross_pay - fedbracket.tax_bracket_6) * 0.37) + 162718)
    else:
        net_pay = "undefined"
