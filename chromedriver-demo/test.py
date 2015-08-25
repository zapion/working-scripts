from selenium import webdriver
from webdriver.common.by import By


def test_parse_page():
    webdriver.Chrome('tool/chromedriver')
    driver.get('https://www.google.com')
    driver.find_element_by_id('lst-ib').send_keys('puffinbrowser')
    driver.find_element(By.CssSelector, 'a[href="/about/"]').click()
    driver.find_element_by_link_text('Please check here for details.').click()
    assert driver.find_element_by_class('jobs-article-table').is_visible()
    assert 'Software Development Engineer in Test' in driver.page_source()
