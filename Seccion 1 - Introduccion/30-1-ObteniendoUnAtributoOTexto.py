# Obtener atributo o texto

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select

class ObtenerTextoAtri(unittest.TestCase):

    def setUp(self):
        global driver
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(chrome_options=options)
        driver.get('https://www.clouditeducation.com/pruebas/index.html')
    
    def testObtenerText(self):
        element = driver.find_element_by_xpath('//*[@id="noImportante"]/td[2]')
        
        if element is not None:
            print(f'Texto: {element.text}')

    def testObtenerAtributo(self):
        element = driver.find_element_by_xpath('//*[@id="importante"]')
        element2 = element.get_attribute("class")
        if element is not None:
            print(f'Clase: {element2}')

    def tearDown(self):
        driver.quit()


if __name__ == '__main__':
    unittest.main()

    