# Unittest mas de un TestCase

import unittest
from selenium import webdriver

class FindByIdName(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get('https://www.clouditeducation.com/pruebas/index.html')
    
    def testId(self):
        elementById = driver.find_element_by_id('noImportante')
        if elementById is not None:
            print('Encontramos el elemento con id = noImportante')

    def testIdName(self):
        elementByName = driver.find_element_by_name('ultimo')
        if elementByName is not None:
            print('Encontramos el elemento con name = ultimo')

    def tearDown(self):
        driver.quit()

if __name__=="__main__":
    unittest.main()
