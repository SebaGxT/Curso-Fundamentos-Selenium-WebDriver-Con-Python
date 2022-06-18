# Cambiar foco a una alerta

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class CambiarFocoAlert(unittest.TestCase):

    def setUp(self):
        global driver
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(chrome_options=options)
        driver.get('https://www.clouditeducation.com/pruebas/index.html')

    def testCambiaAlert(self):
        
        driver.find_element(By.XPATH,'//*[@id="center"]/button').click()
        time.sleep(3)
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(3)
        
        
    def tearDown(self):
        driver.quit()

if __name__ == '__main__':
    unittest.main()

