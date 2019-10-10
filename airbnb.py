
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
class Airbnb():
    def booking(self):
        #Launch the browser
        driver = webdriver.Chrome(executable_path ="/Users/admin4/Desktop/chromedriverforselenium/chromedriver.exe")
        #Enter the Url
        driver.get("https://www.airbnb.ca/")
        #find the numbers of links in home page
        links=driver.find_elements_by_tag_name("a")
        print("Number of links present: ", len(links))
        #enter booking details
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//input[@id='Koan-magic-carpet-koan-search-bar__input']").send_keys("Toronto, ON")
        driver.implicitly_wait(5)
        driver.find_element_by_id("checkin_input").click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//td[@class='_16zigr23'][contains(text(),'12')]").click()
        driver.implicitly_wait(5)
        # mouse operation
        actions=ActionChains(driver)
        x=driver.find_element_by_xpath("//input[@id='checkout_input']")
        driver.implicitly_wait(5)
        y=driver.find_element_by_xpath("//td[@class='_16zigr23'][contains(text(),'23')]")
        actions.move_to_element(x).move_to_element(y).click().perform()
        driver.implicitly_wait(5)

        driver.find_element_by_xpath("//button[@class='_7ykwo4']").click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//div[@class='_9cfq872']//div//div[1]//div[1]//div[1]//div[1]//div[2]//div[1]//div[3]//button[1]").click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//button[@class='_b0ybw8s']").click()
        driver.implicitly_wait(5)
        # search
        driver.find_element_by_xpath("//span[@class='_ftj2sg4']").click()
        #Screen shot
        driver.get_screenshot_as_file("/Users/admin4/Desktop/screenshot.png")
        driver.maximize_window()
        driver.implicitly_wait(5)
        #Scroll by
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
        driver.quit()
anb=Airbnb()
anb.booking()
