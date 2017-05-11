# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://gzfa.xdz.com.cn/ModuleBook/PersonalRentBook/Index"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled(self):
        driver = self.driver
        driver.get(self.base_url + "/ModuleBook/PersonalRentBook/Index")
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | iframeDialog | ]]
        driver.find_element_by_xpath("//td[24]/div/div").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_xpath("//button[@type='button']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | iframeDialog | ]]
        driver.find_element_by_css_selector("span.room-no.clear").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_xpath("//button[@type='button']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | iframeDialog | ]]
        Select(driver.find_element_by_id("RoomTypeID")).select_by_visible_text(u"蓝C6号楼A")
        driver.find_element_by_xpath("//tr[4]/td[7]/div/div").click()
        driver.find_element_by_xpath("//tr[11]/td[7]/div/div").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_xpath("//div[4]/div/a/span").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | iframeDialog | ]]
        driver.find_element_by_xpath("//tr[11]/td[9]/div/div").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_css_selector("span.ui-icon.ui-icon-closethick").click()
        driver.find_element_by_css_selector("input.button").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

