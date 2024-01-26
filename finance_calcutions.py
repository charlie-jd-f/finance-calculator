def simple_interest(deposit, rate, time):
    A = deposit*(1+(rate/100)*time)
    return A

def compound_interest(deposit, rate, time):
    A = deposit*(1+(rate/100))**time
    return A

def bond_repayment(value, rate, time):
    rate = rate/(100*12)
    A = (rate*value)/(1-(1+rate)**(-time))
    return A