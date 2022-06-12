# Busqueda general de elementos

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class FindElement(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get('https://www.clouditeducation.com/pruebas/index.html')
    
    def testFindElement(self):
       element = driver.find_element(By.ID,'primera')
       if element is not None:
        print('Elemento Encontrado')

       element = driver.find_element(By.XPATH,'/html/body/div/div[2]/h1[2]')
       if element is not None:
        print('Elemento Xpath Encontrado')
    
    def tearDown(self):
        driver.quit()

if __name__ == '__main__':
    unittest.main()
