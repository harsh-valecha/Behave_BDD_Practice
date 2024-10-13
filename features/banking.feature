Feature: Banking operations
  Scenario: Successful withdrawal
    Given my account balance is 100
    When I withdraw 40
    Then my account balance should be 60

  Scenario: Successful deposit
    Given my account balance is 100
    When I deposit 50
    Then my account balance should be 150
