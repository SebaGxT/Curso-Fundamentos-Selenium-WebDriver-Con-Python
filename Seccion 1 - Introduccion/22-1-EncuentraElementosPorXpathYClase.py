# Encontrar elementos por Xpath y por Clase

import unittest
from selenium import webdriver

class FindByXpathClass(unittest.TestCase):
    
    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get('https://www.clouditeducation.com/pruebas/index.html')
    
    def testByXpath(self):
        elementXpath = driver.find_element_by_xpath('//*[@id="noImportante"]/td[1]')
        if elementXpath is not None:
            print('Elemento Xpath encontrado')

    def testByClass(self):
        elementClass = driver.find_element_by_class_name('rojo')
        if elementClass is not None:
            print('Elemento con clase Rojo encontrado')

    def tearDown(self):
        driver.quit()

if __name__=="__main__":
    unittest.main()

    
    
    
