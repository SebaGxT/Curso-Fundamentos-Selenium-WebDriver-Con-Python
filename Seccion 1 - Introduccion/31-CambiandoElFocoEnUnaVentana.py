# Cambiar foco de pagina

'''
Propiedades de manejo del navegador

current_url -> url de la pagina
current_window_handle -> handle de la ventana actual
name -> nombre del navegador
orientation -> orientacion del dispositivo
page_source -> codigo de la pagina
title -> titulo de la pagina
window_handles -> los handles de todas  las ventanas en la sesion actual

cambio a otra ventana alerta o frame

switch_to.window()
switch_to.alert()
switch_to.frame()

'''

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class CambiarFoco(unittest.TestCase):

    def setUp(self):
        global driver
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(chrome_options=options)
        driver.get('https://www.clouditeducation.com/pruebas/index.html')
    

    def testCambiaVentana(self):

        url = driver.current_window_handle
        print(f'El handle actual es: {url}')

        driver.find_element(By.XPATH,'//*[@id="Buton1"]').click()

        urls = driver.window_handles
        print(f'Todos los handles: {urls}')

        time.sleep(3)

        for url in urls:
            if url != urls:
                driver.switch_to.window(url)
                break

        time.sleep(3)     

    def tearDown(self):
        driver.quit()

if __name__ == '__main__':
    unittest.main()