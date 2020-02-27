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

class TestB():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_b(self):
    self.driver.get("https://ielts.neea.edu.cn/")
    self.driver.set_window_size(1366, 727)
    self.driver.find_element(By.ID, "btn_log_goto").click()
    self.driver.find_element(By.LINK_TEXT, "考位查询").click()
    self.driver.find_element(By.ID, "2020-04").click()
    self.driver.find_element(By.ID, "mvfSiteProvinces211").click()
    self.driver.find_element(By.ID, "btnSearch").click()
    self.driver.find_element(By.CSS_SELECTOR, ".table:nth-child(1) tr:nth-child(1) > td:nth-child(6)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".table:nth-child(1) tr:nth-child(2) > td:nth-child(6)").click()
  
