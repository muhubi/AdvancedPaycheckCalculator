# import gross
# import fed
#
# fed.annual_gross_pay = gross.gross_pay * gross.basepay.pay_periods


class filers_state:
    state = input("What state will you be filing your income in? Enter your state's two letter"
                  "abbreviation: ").upper()

    state_no_tax = ["AK", "FL", "NH", "NV", "SD", "TN", "TX", "WA", "WY"]
    state_flat_tax = ["CO", "IL", "IN", "KY", "MA", "MI", "NC", "PA", "UT"]
    state_graduated_tax = ["AL", "AZ", "AR", "CA", "CT", "DE", "GA", "HI", "ID", "IA", "KS", "LA",
                           "ME", "MD", "MN", "MS", "MO", "MT", "NE", "NJ", "NM", "NY", "ND", "OH",
                           "OK", "OR", "RI", "SC", "VT", "VA", "WV", "WI", "DC", "D.C."]

    if state in state_no_tax:
        print("Congratulations! You have no state income tax!")
    elif state in state_flat_tax:
        print("Your state has a flat tax rate for income tax.")
    elif state in state_graduated_tax:
        print('Your state uses a Graduated-rate system for state income tax.')
    else:
        print("Please enter your state using only the 2 letter official abbreviation!")