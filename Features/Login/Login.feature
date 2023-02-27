Feature: Login functionality
  Scenario: Login
    Given User on login page
    When User enter "student" and "Password123"
    And User click on login button
    Then Would show the user page