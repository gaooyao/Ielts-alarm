# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestD():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_d(self):
    self.driver.get("https://ielts.neea.edu.cn/")
    self.driver.set_window_size(1366, 728)
    self.driver.find_element(By.ID, "btn_log_goto").click()
    self.driver.find_element(By.ID, "userId").click()
    self.driver.find_element(By.ID, "userId").send_keys("53029506")
    self.driver.find_element(By.ID, "userPwd").click()
    self.driver.find_element(By.ID, "userPwd").send_keys("Goyo1122")
    self.driver.find_element(By.ID, "checkImageCode").click()
    self.driver.find_element(By.ID, "checkImageCode").send_keys("zeyd")
    self.driver.find_element(By.ID, "checkImageCode").send_keys(Keys.ENTER)
    self.driver.find_element(By.ID, "btn_log_goto").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(14) > a").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(10) > a").click()
  
