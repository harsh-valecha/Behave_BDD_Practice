from pytest_bdd import scenarios, given, when, then

# Load feature file scenarios
scenarios('../features/banking.feature')

# Global variable for account balance
balance = 0

@given('my account balance is 100')
def set_balance():
    global balance
    balance = 100

@when('I withdraw 40')
def withdraw():
    global balance
    balance -= 40

@when('I deposit 50')
def deposit():
    global balance
    balance += 50

@then('my account balance should be 60')
def check_withdraw_balance():
    assert balance == 60

@then('my account balance should be 150')
def check_deposit_balance():
    assert balance == 150
