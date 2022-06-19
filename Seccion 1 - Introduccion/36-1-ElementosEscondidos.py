# Elementos Escondidos

import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class ElementosEscondidos(unittest.TestCase):

    def setUp(self):
        global driver
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(chrome_options=options)
        driver.get('https://www.clouditeducation.com/pruebas/index.html')
        driver.implicitly_wait(15)
    
    def testElementosEscondidos(self):
        btn = driver.find_element(By.ID,'proceed')

        if btn is not None:
            btn.click()
        
        time.sleep(3)

    def tearDown(self):
        driver.quit()

if __name__ == '__main__':
    unittest.main()

