# POM Page Object Model

'''

Page Objects

Page Object Model (POM) es un patrón de diseño. O en otras palabras es una estrategia probada para optimizar la creación de tus pruebas, este modelo
ofrece las siguentes ventajas.

    - Tu código será más fácil de entender
    - Fácil de mantener por cualquier persona
    - Código reusable - use el mismo script en varias pruebas

'''
import sys
sys.path.append(r'C:\Users\gueri\Desktop\Programacion y otros\Cursos\Fundamentos Selenium WebDriver Con Python\Seccion 1 - Introduccion\PageObjects')
import unittest
from selenium import webdriver
from paginas.loginPaginas import LoginPage
from paginas.pagina2 import Page2

class PruebaPOM(unittest.TestCase):

    def setUp(self):
        global driver
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(chrome_options=options)
        driver.get('https://www.clouditeducation.com/pruebas/loginTest.html')

    def testLogin(self):
        
        pl = LoginPage(driver)
        MN = Page2(driver)

        pl.login('Sebastian','Password')
        MN.meterNombre('Sebastian')

    def tearDown(self):
        driver.quit()

if __name__ == '__main__':
    unittest.main()