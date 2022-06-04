# Predicados en Xpath

'''

//elemento[1] <- los array comienzan desde 1 - selecciona el primer elemento
//elemento[last()] <- selecciona el ultimo elemento
//elemento[last()-1] <- anteultimo
//elemento[position()<3] <- selecciona todo hasta la posicion 2
//elemento[@id] <- seleccion todos los elementos que contengan id
//elemento[@id = "nombre"] <- selecciona el elemento con el id especifico
//elemento[@atributo = valor] <- selecciona todos los elementos que contenga ese atributo y ese valor
//* <- selecciona todos los nodos
//elemento//* <- selecciona todos los elementos debajo del seleccionado
//*[@*] <- selecciona todos los elementos con uno o mas atributos

'''

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://google.com.ar')
driver.quit()