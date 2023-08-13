from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_google_calc():
    url = 'http://www.google.com/'
    search_word = 'Калькулятор'

    browser = webdriver.Chrome()
    browser.get(url)
    browser.maximize_window()

    search = browser.find_element(By.ID, "APjFqb")
    search.send_keys(search_word)
    button = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.NAME, "btnK")))
    button.click()
    numb_1 = browser.find_element(By.CSS_SELECTOR, "div[jsname='N10B9']")
    numb_1.click()
    browser.find_element(By.CSS_SELECTOR, "div[jsname='YovRWb']").click()
    browser.find_element(By.CSS_SELECTOR, "div[jsname='lVjWed']").click()
    browser.find_element(By.CSS_SELECTOR, "div[jsname='pPHzQc']").click()
    browser.find_element(By.CSS_SELECTOR, "div[jsname='KN1kY']").click()
    browser.find_element(By.CSS_SELECTOR, "div[jsname='XSr6wc']").click()
    numb_1.click()
    browser.find_element(By.CSS_SELECTOR, ".UUhRt").click()

    # Проверка ОР и ФР

    memory_string = browser.find_element(By.CSS_SELECTOR, "div[class*=XH1CIc]").text
    result_string = browser.find_element(By.CSS_SELECTOR, "div[class*=z7BZJb]").text
    expected_memory_string = '1 × 2 - 3 + 1 ='
    expected_result_string = "0"
    browser.close()

    assert expected_memory_string == memory_string and result_string == expected_result_string



