# Framework UnitTest

import unittest
from selenium import webdriver

class FindByIdName(unittest.TestCase):

    # La primer funcion se debe llamar setup - se encarga de inicializar el driver
    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get('https://www.clouditeducation.com/pruebas/index.html')

    # El nombre de la prueba debe empezar por test
    def testIdName(self):
        elementById = driver.find_element_by_id('noImportante')
        if elementById is not None:
            print('Encontramos el elemento con id = noImportante')
        elementByName = driver.find_element_by_name('ultimo')
        if elementByName is not None:
            print('Encontramos el elemento con name = ultimo')

    # tearDown - se usa para cerrar la ejecucion
    def tearDown(self):
        driver.quit()

# La condicion es una forma estandar en python para asegurarse que este unittest esta corriendo como programa independiente y no es llamado de otro modulo
# Esto no es necesario si no se lo llama desde otro modulo
if __name__=="__main__":
    unittest.main()