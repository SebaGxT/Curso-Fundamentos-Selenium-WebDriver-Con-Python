# Encontrar elementos de link por el texto

import unittest
from selenium import webdriver

class elementLinkText(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get('https://www.clouditeducation.com/pruebas/index.html')
    
    def testElementByLinkText(self):
        elementLink = driver.find_element_by_link_text('Pagina 2')
        if elementLink is not None:
            print('Elemento Link encontrado')
    
    def testElementByPatialLinkText(self):
        elementLink = driver.find_element_by_partial_link_text('four')
        if elementLink is not None:
            print('Elemento Link encontrado')

    def tearDown(self):
        driver.quit()

if __name__ == '__main__':
    unittest.main()
