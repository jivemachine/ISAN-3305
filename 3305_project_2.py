# setting global variables
global MIN_BALANCE
global OVERDRAFT_FEE
global users_money

# global CONST
MIN_BALANCE = 0.00
OVERDRAFT_FEE = 20.00

# global var
users_money = 0.00

def check_balance(users_money):
    print(f"${round(users_money, 2)}")


def deposit(users_money, deposit):
    users_money = users_money + deposit
    return users_money

def withdraw(users_money, withdraw):
    # handle overdraft fees
    if (users_money >= MIN_BALANCE):
        users_money = users_money - withdraw
    else:
        users_money = users_money - withdraw
        users_money = users_money - OVERDRAFT_FEE
    # return users money
    return users_money

def display_menu():
    choices = ["check balance ", "withdraw from your account ", "deposit funds ", "exit"]
    print("Would you like to:")
    i = 1
    for choice in choices:
        print(choice)
        print(f"press {i}\n")
        i += 1



def main():
    #check_balance(users_money)

    #updated_money = deposit(users_money, 5)

    #check_balance(updated_money)

    #updated_money = withdraw(updated_money, 5)

    #check_balance(updated_money)
    display_menu()



    

main()
