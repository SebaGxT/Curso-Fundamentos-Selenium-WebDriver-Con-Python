# Acciones - Hacer click y escribir

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class AccionesEnElementos(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get('https://www.clouditeducation.com/pruebas/index.html')
    
    def testAccionar(self):
        element = driver.find_element(By.XPATH,'//a[contains(text(),"Pagina 2")]')
        element.click()
        
        element2 = driver.find_element(By.ID,'Segundo')
        if element2 is not None:
            element2.send_keys('Sebastian')
            time.sleep(5)
        else:
            time.sleep(5)
            print('Elemento no encontrado')

    def tearDown(self):
        driver.quit()


if __name__ == '__main__':
    unittest.main()