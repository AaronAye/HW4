from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open Target page HW 4')
def open_target(context):
    context.driver.get('https://www.target.com/')
    sleep(5)


@when("Verify target circle HW")
def input_search(context):
    context.driver.find_elements(By.XPATH, value="//a[@id='utilityNav-circle']").click()
    links = context.driver.find_elements(By.XPATH, value="//div[@class='cell-item-content']")
    print(len(links))
    assert len(links) == 10, f"Expected 10 links, but got {len(links)}"
    sleep(5)






