#!/usr/bin/env python
# -*- coding: utf-8 -*-  
from selenium import webdriver
browser = webdriver.Firefox()
browser.get("http://www.baidu.com")
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
browser.quit()


driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
print "浏览器最大化"
driver.maximize_window() #将浏览器最大化显示
driver.quit()