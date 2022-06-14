# Seleccion de opcion en menu desplegable

'''
Clase select de selenium

deselect_all() -> en elementos de opcion multiple remueve todas las selecciones
deselect_by_index(index) -> Remueve la seleccion basado en la posicion o indice
deselect_by_value(value) -> remueve por valor
deselect_by_visible_text(text) -> remueve por texto desplegado
select_by_index(index) -> selecciona por indice
select_by_value(value) -> selecciona por valor
select_by_visible_text(text) -> selecciona por texto visible

'''

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class SeleccionOpcionMenu(unittest.TestCase):


    def setUp(self):
        global driver
        options = webdriver.ChromeOptions() 
        options.add_argument("--start-maximized") 
        driver = webdriver.Chrome(chrome_options=options)
        driver.get('https://www.clouditeducation.com/pruebas/index.html')
    

    def testSeleccionOpcion(self):
        element = driver.find_element(By.NAME,'ingrediente')
        if element is not None:
            elementSel = Select(element)
            elementSel.select_by_value('cebolla')
            time.sleep(5)
    
    def testSeleccion(self):
        element2 = driver.find_element_by_name('Select1')
        if element2 is not None:
            elementSel = Select(element2)
            elementSel.select_by_index(1)
            elementSel.select_by_value('manzana')
            elementSel.select_by_visible_text('Naranja')
            time.sleep(5)

    def tearDown(self):
        driver.quit()

if __name__ == '__main__':
    unittest.main()
