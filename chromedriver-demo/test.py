from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep


def test_parse_page():
    driver = webdriver.Chrome('tool/chromedriver')
    driver.get('https://www.google.com')
    input_field = driver.find_element_by_id('lst-ib')
    input_field.send_keys('puffinbrowser')
    input_field.submit()
    #menu_button = driver.find_elements(By.CSS_SELECTOR, '.sbsb_g input')[0]
    #if not menu_button.is_displayed():
    #    menu_button = driver.find_elements(By.CSS_SELECTOR, 'input[name="btnK"]')[0]
    #menu_button.click()
    ires = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, 'ires')))
    driver.find_element(By.CSS_SELECTOR, 'a[href="https://www.puffinbrowser.com/"]').click()
    driver.find_element(By.CSS_SELECTOR, 'a[href="/about/"]').click()
    driver.find_element_by_link_text('Please check here for details.').click()
    # Verification
    assert driver.find_element_by_class_name('jobs-article-table').is_displayed()
    assert 'Software Development Engineer in Test' in driver.page_source
