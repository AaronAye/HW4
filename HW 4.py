from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By


@given("Open Target main page hw4")
def open_target(context):
    context.driver.get('https://www.target.com/')
    sleep(5)


@when("Search for {search_text} hw4")
def input_search(context, search_text):
    context.driver.find_element(By.ID,'search').send_keys(search_text)
    context.driver.find_element(By.XPATH, value="//button[@data-test='@web/Search/SearchButton']").click()

@then("Click on cart icon hw4")
def target_search(context):
    context.driver.find_element(By.XPATH, value="//div[@data-test='@web/CartIcon']").click()

