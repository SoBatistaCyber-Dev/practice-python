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
    
    first_deduction = min(10000, income)
    income -= first_deduction
    first_bracket_tax = first_deduction * 0

    second_deduction = min(10000, income)
    income -= second_deduction
    second_bracket_tax = second_deduction * 0.1
    
    third_deduction = income
    third_bracket_tax = third_deduction * 0.2
 
    print("Your taxes are:", int(first_bracket_tax + second_bracket_tax + third_bracket_tax))


income = int(input("Enter your income: "))
income_tax(income)