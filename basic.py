print('Hello world')


## If Statements
## If buyers have a good credit, they has a better down payment.
price = 1
is_good_credit = True


if is_good_credit:
    down_payment = price * 0.1
else:
    down_payment = price *0.2

print(f"Down payment: ${down_payment}")


## Logical operators
## Eligible for loan, if you have high income AND good credit

has_high_income = False
has_good_credit = True

if has_high_income and has_good_credit:
    eligible_loan = True
else:
    eligible_loan = False

print(eligible_loan)


## name must be at least 3 characters

name = "aasdfasdfasdfbgh"

if len(name) <= 3:
    print("name must be at least 3 characters.")
elif len(name) > 10:
    print("no more than 10")
else:
    print("it is OK")
