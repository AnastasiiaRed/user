from django.test import LiveServerTestCase
from selenium import webdriver
import time
from django.contrib.auth.models import User
	
class SeleniumTests(LiveServerTestCase):
    def test_auth(self):
        br = webdriver.Opera()
        br.get('http://localhost:8000/register/')
        time.sleep(3)
        br.find_element_by_name('email').send_keys('test12345@gmail.com')
		br.find_element_by_name('username').send_keys('test12345')
        br.find_element_by_name('password1').send_keys('123456Pp')
		br.find_element_by_name('password2').send_keys('123456Pp')
        br.find_element_by_name('btn_register').click()
		time.sleep(3)
		Assert.assertEquals(driver.getPageSource().contains("Account created successfully. Check email to verify the account."), true);
		
		
        br.quit()