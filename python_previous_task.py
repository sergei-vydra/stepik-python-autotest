import time, math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 20).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    button = browser.find_element_by_id("book")
    button.click()

    browser.execute_script("window.scrollTo(0, 100)")

    input_value = browser.find_element_by_id("input_value")
    input_value_text = input_value.text

    result = calc(input_value_text)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(result)

    submit = browser.find_element_by_id("solve")
    submit.click()
finally:
    time.sleep(10)
    browser.quit()