Feature: Google Search Operations
  Scenario: google search with selenium
    Given The user is at google search page
    When User searches for a selenium tutorials
    Then Search results should display selenium tutorials