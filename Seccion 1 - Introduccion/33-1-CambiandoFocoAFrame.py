# Cambiar foco a Frame

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class CambiarFocoAFrame(unittest.TestCase):

    def setUp(self):
        global driver
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(chrome_options=options)
        driver.get('https://www.clouditeducation.com/pruebas/index.html')
    
    def testCambioAFrame(self):
        element = driver.find_element(By.ID,'pruebas-iframe')

        if element is not None:
            driver.switch_to.frame(element)

            element2 = driver.find_element(By.ID,'Segundo')
            
            if element2 is not None:
                element2.send_keys('Sebastian')
                time.sleep(5)

    def tearDown(self):
        driver.quit()

if __name__ == '__main__':
    unittest.main()