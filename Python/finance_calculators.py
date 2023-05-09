import math

# Bellow I will create a calculator allowing the user to calculate their investment or bond
# First the user will have to select which calculator to use and input some data for the calculations
# Then a statement structure will be created to account for different user data inputs
char = "***********"
print(f"{char}Investment - to calculate the amount you will earn on your investment.{char}")
print(f"{char}Bond - to calculate the amount you will have to pay on a home loan.{char}")

while True:
        chosen_calculation = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# Here I created the loop and functions to calculate the investment interest.
        try:
                if chosen_calculation == "investment":                     
                        amount_to_be_deposited = int(input("What amount do you wish to deposit?: "))
                        user_chosen_interest = int(input("Type your interest rate: "))
                        years_to_be_invested = int(input("For how many years do you wish to invest?: "))
                        interest = input("You can choose 'simple' or 'compound' interest. Type your choice: ").lower()
                                               
                        if interest == "simple":
                                simple_interest_calculator = amount_to_be_deposited * (1 + (user_chosen_interest / 100) * years_to_be_invested)
                                total_simple_interest = print(f"After {years_to_be_invested} years, with {user_chosen_interest}% as interest, your final amount will be £{simple_interest_calculator: .2f}. An increase of £{simple_interest_calculator - amount_to_be_deposited: .2f}.")
                        # Compound interest calculator
                        else:
                                compound_interest_calculator = amount_to_be_deposited * math.pow(1 + (user_chosen_interest / 100),years_to_be_invested)
                                total_compound_interest = print(f"After {years_to_be_invested} years, with {user_chosen_interest}% as interest, your final amount will be £{compound_interest_calculator: .2f}. An increase of £{compound_interest_calculator - amount_to_be_deposited: .2f}.")

                        break

# Here I have created the loop and functions for the bond, to calculate the monthly repayment amount.
                elif chosen_calculation == "bond":
                        house_value = int(input("What is your current house value?: "))
                        your_interest_rate = int(input("Type your interest rate: "))
                        borrowing_lenght = int(input("In how many months do you plan to repay the bond?: "))
                        bond_repayment_calculator = (((your_interest_rate / 100) / 12) * house_value) / (1 - (1 + ((your_interest_rate / 100) / 12)) ** (- borrowing_lenght))
                        monthly_repayment = print(f"Your monthly repayments will be £{bond_repayment_calculator: .2f}, for {borrowing_lenght} months. ")

                        break

                else:
                        print("Invalid choice")

        except:
                 print("Invalid input. Plrease try again.")
        
                