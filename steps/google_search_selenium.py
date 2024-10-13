from behave import given , when , then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('The user is at google search page')
# open chrome browser and google search page
def open_chrome(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.google.com/')


@when('User searches for a {keyword}')
def search_keyword(context,keyword):
    search_box = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys(keyword)  # Type in the search box
    search_box.send_keys(Keys.RETURN)  # Press Enter

@then('Search results should display {keyword}')
def check_results(context,keyword):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )
    assert keyword in context.driver.page_source
