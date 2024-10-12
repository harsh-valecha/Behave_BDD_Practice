from behave import given , when , then

balance = 0

@given('my account balance is {account_balance}')
def set_balance(context , account_balance):
    global balance
    balance = float(account_balance)
    print(f'The Balance of Account is :{balance:.2f}')

@when('I withdraw {amount}')
def withdraw(context , amount):
    global balance
    balance-=float(amount)
    print(f'The Balance of Account is :{balance:.2f}')

@then('my account balance should be {final_amount}')
def check_balance(context , final_amount):
    global balance
    final_amount = float(final_amount)
    assert balance == final_amount , 'Final amount not matches with account balance'

@when('I deposit {amount}')
def deposit(context , amount):
    global balance
    balance +=float(amount)
    print(f'The Balance of Account is :{balance:.2f}')
