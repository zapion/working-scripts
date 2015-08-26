import time
from appium import webdriver

# capabilities for built-in email app
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.android.email'
desired_caps['appActivity'] = 'com.android.email.activity.Welcome'

# email locator index
email_prefix = 'com.android.email:id/'
to_field_locator = email_prefix + 'to'
subject_field_locator = email_prefix + 'subject'
body_field_locator = email_prefix + 'body'

send_button_locator = email_prefix + 'send'
compose_button_locator = email_prefix + 'compose_button'
conversation_list_view_locator = email_prefix + 'conversation_list_view'
delete_button_locator = email_prefix + 'delete'
title_locator = email_prefix + 'subject_and_folder_view'


def test_send_mail():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    
    compose = driver.find_element_by_id(compose_button_locator)
    if compose.is_displayed():
        compose.click()
    
    to = driver.find_element_by_id(to_field_locator)
    subject = driver.find_element_by_id(subject_field_locator)
    body = driver.find_element_by_id(body_field_locator)
    send = driver.find_element_by_id(send_button_locator)
    
    to.send_keys('zapionator@gmail.com') # FIXME use a default test email
    subject.send_keys('Verify sending email')
    body.send_keys('Hello, this is a test from the testing script')
    send.click()
    
    # Verification
    conversation_list = driver.find_element_by_id(conversation_list_view_locator)
    els = conversation_list.find_elements_by_class_name('android.widget.FrameLayout')
    loc_1 = els[0].location 
    loc_2 = els[3].location
    driver.swipe(loc_1['x'], loc_1['y'], loc_2['x'], loc_2['y'], 800)
    time.sleep(5)
    conversation_list.find_elements_by_class_name('android.widget.FrameLayout')[0].click()
    assert 'Verify sending email Inbox' == driver.find_element_by_id(title_locator)
    driver.find_element_by_id(delete_button_locator).click()
    driver.quit()
