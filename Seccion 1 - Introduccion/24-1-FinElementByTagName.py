# Tag Name

from lib2to3.pgen2 import driver
import unittest
from selenium import webdriver

class findElementTagName(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get('https://www.clouditeducation.com/pruebas/index.html')
    
    def testElementTagName(self):
        elementTag = driver.find_element_by_tag_name('h3')
        if elementTag is not None:
            print('Elemento Tag encontrado')

    def testElementCss(self):
        elementCss = driver.find_element_by_css_selector('#primera')
        if elementCss is not None:
            print('Css Selector Encontrado')

    def tearDown(self):
        driver.quit()

if __name__ == '__main__':
    unittest.main()