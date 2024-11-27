'''
    Calculate income tax

    Calculate income tax for the given income by adhering to the rules below
    Taxable     Income	    Rate (in %)
    First       $10,000	    0
    Next        $10,000	    10
    The         remaining	20

    Expected Output:

    For example, suppose the income is 45000, and the income tax payable is

    10000*0% + 10000*10%  + 25000*20% = $6000.
'''

def income_tax(income):
    if income >= 10000:
        income = income - 10000
        first_bracket_tax = 10000 * 0
        second_bracket_tax = 0
        third_bracket_tax = 0
        if income >= 10000:
            income = income - 10000
            second_bracket_tax = 10000 * 0.1    
            if income > 0:
                third_bracket_tax = income * 0.2
            print("Your taxes are: $", int(first_bracket_tax + second_bracket_tax + third_bracket_tax))
        else:    
            print("Your taxes are: $", int(first_bracket_tax + (income * 0.1)))
    else:
        print("Your taxes are: $", int(income * 0))

income = int(input("Enter your income: "))
income_tax(income)