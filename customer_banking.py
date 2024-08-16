# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input('What is your initial savings account balance? '))
    savings_interest = float(input('What is the APR for the savings account? '))
    savings_maturity = int(input('What is the length in months for your savings account? '))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print("The interest earned is : $", format(savings_data.get_balance(), ',.2f')
    print("The updated CD account balance is : $", format(savings_data.get_balance(), ',.2f') 

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input('What is your initial CD account balance? '))
    cd_interest = float(input('What is the APR for the CD account? '))
    cd_maturity = int(input('What is the length in months for your CD? '))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print("The interest earned is : $", format(cd_account_data.get_balance(), ',.2f')
    print("The updated CD account balance is : $", format(cd_account_data.get_interest(), ',.2f') 


if __name__ == "__main__":
    # Call the main function.
    main()
