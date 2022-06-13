# Seleccionar Radio button y Check Box

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class RadioButtonCheckBox(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get('https://www.clouditeducation.com/pruebas/index.html')

    def testRadio(self):
        element = driver.find_element(By.XPATH,"//input[@id='RadioGroup1_0']")

        if element is not None:
            element.click()

        time.sleep(5)

        element = driver.find_element(By.XPATH,"//input[@id='RadioGroup1_1']")

        if element is not None:
            element.click()

        time.sleep(5)  

    def testCheck(self):
        
        element = driver.find_element(By.XPATH,'//input[@id="CheckboxGroup1_0"]')
        if element is not None:
            element.click()
        
        time.sleep(5)

        element = driver.find_element(By.XPATH,'//input[@id="CheckboxGroup1_1"]')
        if element is not None:
            element.click()

        time.sleep(5)

    def tearDown(self):
        driver.quit()

if __name__ == '__main__':
    unittest.main()

