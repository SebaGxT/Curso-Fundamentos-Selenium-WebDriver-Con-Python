# Acciones en Cadena

import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class AccionesEnCadena(unittest.TestCase):

    def setUp(self):
        global driver
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(chrome_options=options)
        driver.get('https://www.clouditeducation.com/pruebas/index.html')
    
    def testAccionEnCadena(self):
        btn = driver.find_element(By.CLASS_NAME,'dropbtn')

        if btn is not None:
            acciones = ActionChains(driver)
            acciones.move_to_element(btn).perform()

            lnk = driver.find_element(By.XPATH,'/html/body/div/div[2]/div[1]/div/a[1]')

            if lnk is not None:
                acciones.move_to_element(lnk)
                acciones.click(lnk)
                acciones.perform()
            
        time.sleep(5)

    def tearDown(self):
        driver.quit()

if __name__ == '__main__':
    unittest.main()
