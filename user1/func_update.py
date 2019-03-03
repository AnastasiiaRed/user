from django.test import LiveServerTestCase
from selenium import webdriver
import time
from django.contrib.auth.models import User
from django.test import TestCase
	
class SeleniumTests(LiveServerTestCase):
    def test_auth(self):
        br = webdriver.Opera()
        br.get('http://localhost:8000')
        time.sleep(3)
        update=br.find_element_by_xpath('//a[contains(@href,"edit/2")]')
        update.click()
        time.sleep(6)
        br.find_element_by_name('name').send_keys('Анастасия123')
        br.find_element_by_name('lname').send_keys('test12345@gmail.com')
        br.find_element_by_name('password').send_keys('123456Pp')
        br.find_element_by_name('bdate').send_keys('23.04.1997')
        time.sleep(3)
        br.find_element_by_name('save').click()
        time.sleep(6)
        assert "Анастасия123" in br.page_source
		
		