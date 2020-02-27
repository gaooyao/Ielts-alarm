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

class TestA():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_a(self):
    self.driver.get("https://ielts.neea.edu.cn/")
    self.driver.set_window_size(1382, 744)
    self.driver.find_element(By.ID, "btn_log_goto").click()
    self.driver.execute_script("window.scrollTo(0,162)")
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(14) > a").click()
    self.driver.find_element(By.ID, "2020-03").click()
    self.driver.find_element(By.ID, "mvfSiteProvinces211").click()
    self.driver.find_element(By.ID, "mvfSiteProvinces212").click()
    self.driver.find_element(By.ID, "btnSearch").click()
  
