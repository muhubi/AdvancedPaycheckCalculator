import gross

annual_gross_pay = gross.gross_pay * gross.basepay.pay_periods


class fedbracket:
    # This class should be updated annually to account for the updates tax bracket minimums
    # and maximums for the current fiscal year as updated per the United States IRS
    filing_status = float(input("What is your federal tax filing status? 1 = Single | 2 = Married, filing jointly | "
                                "3 = Married, filing separately | 4 = Head of Household "))
    if filing_status == 1:
        print("Filing status = Single")
        tax_bracket_1 = 9950
        tax_bracket_2 = 40525
        tax_bracket_3 = 86375
        tax_bracket_4 = 164925
        tax_bracket_5 = 209425
        tax_bracket_6 = 523600
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


class taxmax:
    # This class is for calculating the maximum tax rate for the prior tax bracket which is used
    # in the fedpay class to calculate the total tax deductions. This class should not need to
    # be modified except for if the IRS changes the number of tax brackets and/or the percentage
    # that filer are taxed at
    taxmax1 = fedbracket.tax_bracket_1 * 0.1
    taxmax2 = taxmax1 + (fedbracket.tax_bracket_2 - fedbracket.tax_bracket_1) * 0.12
    taxmax3 = taxmax2 + (fedbracket.tax_bracket_3 - fedbracket.tax_bracket_2) * 0.22
    taxmax4 = taxmax3 + (fedbracket.tax_bracket_4 - fedbracket.tax_bracket_3) * 0.24
    taxmax5 = taxmax4 + (fedbracket.tax_bracket_5 - fedbracket.tax_bracket_4) * 0.32
    taxmax6 = taxmax5 + (fedbracket.tax_bracket_6 - fedbracket.tax_bracket_5) * 0.37


class fedpay:
    # This class calculates the total federal tax deduction that is taken from the gross
    # annual pay of the user. This class should not need to be modified except for if
    # the IRS changes the number of tax brackets and/or the percentage that filers are
    # taxed at
    if annual_gross_pay <= fedbracket.tax_bracket_1:
        net_pay = annual_gross_pay * 0.9
    elif fedbracket.tax_bracket_1 < annual_gross_pay <= fedbracket.tax_bracket_2:
        net_pay = annual_gross_pay - (((annual_gross_pay - fedbracket.tax_bracket_1) * 0.12) + taxmax.taxmax1)
    elif fedbracket.tax_bracket_2 < annual_gross_pay <= fedbracket.tax_bracket_3:
        net_pay = annual_gross_pay - (((annual_gross_pay - fedbracket.tax_bracket_2) * 0.22) + taxmax.taxmax2)
    elif fedbracket.tax_bracket_3 < annual_gross_pay <= fedbracket.tax_bracket_4:
        net_pay = annual_gross_pay - (((annual_gross_pay - fedbracket.tax_bracket_3) * 0.24) + taxmax.taxmax3)
    elif fedbracket.tax_bracket_4 < annual_gross_pay <= fedbracket.tax_bracket_5:
        net_pay = annual_gross_pay - (((annual_gross_pay - fedbracket.tax_bracket_4) * 0.32) + taxmax.taxmax4)
    elif fedbracket.tax_bracket_5 < annual_gross_pay <= fedbracket.tax_bracket_6:
        net_pay = annual_gross_pay - (((annual_gross_pay - fedbracket.tax_bracket_5) * 0.35) + taxmax.taxmax5)
    elif fedbracket.tax_bracket_6 < annual_gross_pay:
        net_pay = annual_gross_pay - (((annual_gross_pay - fedbracket.tax_bracket_6) * 0.37) + taxmax.taxmax6)
    else:
        net_pay = "undefined"
