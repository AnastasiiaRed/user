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
        br.find_element_by_name('username').send_keys('test12345@gmail.com')
        time.sleep(3)
        br.find_element_by_name('password').send_keys('123456Pp')
        time.sleep(3)
        br.find_element_by_name('btn_login').click()
		
        br.quit()