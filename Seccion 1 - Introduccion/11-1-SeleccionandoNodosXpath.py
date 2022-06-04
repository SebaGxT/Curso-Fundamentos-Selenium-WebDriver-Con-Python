# Seleccionar nodos con Xpath

'''

/ Selecciona desde la raiz
// Selecciona todos los nodos con un criterio
. Selecciona el nodo actual
.. Selecciona el nodo padre
@ Selecciona atributos

/elemento/segundoelemento/...

//elemento - selecciona la primera que encuentra
//elemento[1] - selecciona el elemento como si fuera un array

seleccionar atributos como el id o class
//@id - selecciona todos los id

seleccionar nodos padre
//elemento/../.. <- cada .. sube un nivel desde el elemento seleccionado



'''

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://google.com.ar')
driver.quit()