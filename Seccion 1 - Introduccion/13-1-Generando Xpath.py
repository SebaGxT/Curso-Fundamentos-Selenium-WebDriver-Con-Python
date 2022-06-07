# Generando Xpath

'''
click derecho en el elemento de la consola y copiar Xpath genera la busqueda por ej: .//*[@id='nombre']/td[posicion]

seleccionar texto del elemento -> .//*[@id='nombre']/td[posicion]/text()

funcion contains -> //elemento[contains(text(),'palabra')]

'''

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://google.com.ar')
driver.quit()