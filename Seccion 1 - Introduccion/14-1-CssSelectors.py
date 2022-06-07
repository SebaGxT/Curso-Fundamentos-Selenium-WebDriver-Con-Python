# CSS Selectores

'''

#id <- # solo se usa para buscar id

elemento#id

[nombre] <- atributos entre corchetes
*[nombre] <- cualquier elemento con el atributo

[atributo = 'nombre'] <- encuentra el especifico

elemento[atributo1 = 'nombre'][atributo2 = 'nombre'] <- busca elementos especificando multiples atributos

.clase <- busca elementos por la clase css
elemento.clase <- elementos especificos con la clase css
elemento.clase>elemento <- busca elementos hijos del elemento con la clase css

elemento,elemento2 <- selecciona todos los elementos listados

[atributo^='nombre'] <- busca elementos con atributos cuyo nombre empiezan con el nombre especificado

[atributo*='nombre'] <- busca elementos con atributos especificando un nombre parcial o parte del nombre

[atributo$='nombre'] <- busca elementos con atributos cuyo nombre terminan con el nombre especificado

'''

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://google.com.ar')
driver.quit()
