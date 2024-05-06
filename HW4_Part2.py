from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By


@given("Open Target main page HW4_Part2")
def open_target(context):
    context.driver.get('https://www.target.com/')
    sleep(5)


@when("Search for {search_text} HW4_Part2")
def input_search(context, search_text):
    context.driver.find_element(By.ID,'search').send_keys(search_text)
    context.driver.find_element(By.XPATH, value="//button[@data-test='@web/Search/SearchButton']").click()

@when("Click on add to cart HW4_Part2")
def target_add_to_cart(context):
    sleep(5)
    context.driver.find_element(By.XPATH, value="//button[@id='addToCartButtonOrTextIdFor16849682']").click()
    sleep(3)
    context.driver.find_element(By.XPATH, value="//button[@data-test='fulfillment-cell-shipping']").click()
    sleep(3)
    context.driver.find_element(By.XPATH, value="//button[@data-test='shippingButton']").click()
    sleep(3)
    context.driver.find_element(By.XPATH, value="//a[contains(text(),'View cart')]").click()


@then('Verify item in cart HW4_Part2')
def item_in_cart(context):
    actual_text = context.driver.find_element(By.XPATH, value="//div[contains(text(),'Lavazza Classico Medium Roast Ground Coffee - 12oz')]")
    assert 'Lavazza Classico Medium Roast Ground Coffee - 12oz' in actual_text.text, f'{actual_text} is NOT in cart'
    print("Test case has passed")