"""Import the Account class from the Account.py file."""
from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    
    balance += interest_earned

    savings_account_data = Account(balance, interest_rate, months)    

# savings_account_balance = float(input('What is your initial CD account balance? '))
# savings_account_interest_rate = float(input('What is the APR for the CD account? '))
# savings_account_maturity = int(input('What is the length of months for your CD? '))

# savings_account_data = Account(savings_account_balance, savings_account_interest_rate, savings_account_maturity)
    
# savings_account_data = Account(balance, interest_rate, months)
    

    # Calculate interest earned
    interest_earned = balance * (interest_rate/100) * (months/12)

    # Update the savings account balance by adding the interest earned
    new_balance = balance + interest_earned

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    balance.set_make(new_balance)

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    interest_rate.set_make(interest_earned)

    # Return the updated balance and interest earned.
    return balance and interest_earned
