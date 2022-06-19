# Esperas explicitas - Explicit Waits

'''
Espera explicita

El webdriver define un tiempo de espera para que ocurra una condicion especifica
si la condicion no ocurre se ejecuta un error y si ocurre la condicion continua la ejecucion de la prueba

expected_conditions

element_to_be_clickeable() -> Espera por un elemento y revisa que sea visible y habilitado para darle clic

element_to_be_selected() -> espera a que el elemento se seleccione

presence_of_element_located() -> espera hasta que el element este disponible en el DOM

title_contains() -> espera que el titulo de la pagina contenga una cadena de caracteres

visibility_of() -> localiza el elemento y espera que sea visible y el tamaño del elemento sea mayor a cero

text_to_be_present_in_element() -> localiza el element y espera que contenga un texto

aler_is_present() -> espera que una alerta exista

'''

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WW

class EsperasExplicitas(unittest.TestCase):

    def setUp(self):
        global driver
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(chrome_options=options)
        driver.get('https://www.clouditeducation.com/pruebas/index.html')
    
    def testEsperaExplicita(self):
       espera = WW(driver,10)
       btn = espera.until(EC.element_to_be_clickable((By.ID,'proceed')))
       if btn is not None:
        btn.click()
        time.sleep(10)

    def tearDown(self):
        driver.quit()

if __name__ == '__main__':
    unittest.main()