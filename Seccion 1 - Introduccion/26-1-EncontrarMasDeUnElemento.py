# Encontrar varios elementos

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class FindElements(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get('https://www.clouditeducation.com/pruebas/index.html')
    
    def testElements(self):
        elements = driver.find_elements(By.XPATH,'//tr')
        if elements is not None:
            cant = len(elements)
            print(f'La cantidad de elementos encontrados es: {cant}')
    
    def testtag(self):
        elements = driver.find_elements_by_tag_name('tr')
        if elements is not None:
            cant = len(elements)
            print(f'La cantidad de elementos encontrados es: {cant}')
            
    def tearDown(self):
        driver.quit()

if __name__ == '__main__':
    unittest.main()
