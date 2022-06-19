# Esperas Implicitas

'''
Espera implicita

webdriver espera por un tiempo maximo determinado para encontrar un elemento
este metodo necesita ser llamado una sola vez por sesion
Configuracion general - la misma espera cada vez que tratas de encontrar un elemento
Funciona durante la sesion o sea hasta que cierre el webdriver

'''

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class ImplicitWaits(unittest.TestCase):

    def setUp(self):
        global driver
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(chrome_options=options)
        driver.get('https://www.clouditeducation.com/pruebas/index.html')
        driver.implicitly_wait(15)
    

    def testImplicitWait(self):
        btn = driver.find_element(By.CLASS_NAME,'dropbtnx')

        if btn is not None:
            acciones = ActionChains(driver)
            acciones.move_to_element(btn).perform()

            lnk = driver.find_element(By.XPATH,'/html/body/div/div[2]/div[1]/div/a[1]')

            if lnk is not None:
                acciones.move_to_element(lnk)
                acciones.click(lnk)
                acciones.perform()

    def tearDown(self):
        driver.quit()

if __name__ == '__main__':
    unittest.main()

