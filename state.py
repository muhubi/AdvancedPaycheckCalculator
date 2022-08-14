import gross
import fed

fed.annual_gross_pay = gross.gross_pay * gross.basepay.pay_periods

global state


class filers_state:
    state = input("What state will you be filing your income in? Enter your state's two letter"
                  "abbreviation: ").upper()

    state_no_tax = ["AK", "FL", "NH", "NV", "SD", "TN", "TX", "WA", "WY"]
    state_flat_tax = ["CO", "IL", "IN", "KY", "MA", "MI", "NC", "PA", "UT"]
    state_graduated_tax = ["AL", "AZ", "AR", "CA", "CT", "DE", "GA", "HI", "ID", "IA", "KS", "LA",
                           "ME", "MD", "MN", "MS", "MO", "MT", "NE", "NJ", "NM", "NY", "ND", "OH",
                           "OK", "OR", "RI", "SC", "VT", "VA", "WV", "WI", "DC", "D.C."]

    if state in state_no_tax:
        state_tax_type = str("Congratulations! Your state has no income tax!")
    elif state in state_flat_tax:
        state_tax_type = str("Your state has a flat tax rate for income tax.")
    elif state in state_graduated_tax:
        state_tax_type = str("Your state uses a Graduated-rate system for state income tax.")
    else:
        state_tax_type = str("Please enter your state using only the 2 letter official abbreviation!")


class filers_state_status:
    status_status = input("What is your state tax filing status? 1 = Single | 2 = Married, filing jointly ")


# Need to account for filing status
class state_deduction:
    if state in filers_state.state_no_tax:
        state_tax_amount = 0
    elif state == "CO":
        state_tax_amount = fed.annual_gross_pay * 0.0455