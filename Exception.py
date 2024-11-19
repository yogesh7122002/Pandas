# Why use else in try/except construct in Python?
# try: and except: are commonly known for exceptional handling in Python, so where does else: come in handy? else: will be triggered when no exception is raised. 

# Example:

# Let’s learn more about else: with a couple of examples.

# On the first try, we entered 2 as the numerator and d as the denominator. Which is incorrect, and except: was triggered with “Invalid input!”. 

# On the second try, we entered 2 as the numerator and 1 as the denominator and got the result 2. No exception was raised, so it triggered the else: printing the message Division is successful. 


try:
    num1 = int(input('Enter Numerator: '))
    num2 = int(input('Enter Denominator: '))
    division = num1/num2
    print(f'Result is: {division}')
except:
    print('Invalid input!')
else:
    print('Division is successful.')


## Try 1 ##
# Enter Numerator: 2
# Enter Denominator: d
# Invalid input!

## Try 2 ##
# Enter Numerator: 2
# Enter Denominator: 1
# Result is: 2.0
# Division is successful.

