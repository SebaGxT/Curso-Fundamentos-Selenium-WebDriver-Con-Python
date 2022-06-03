from selenium import webdriver #Primero hay que importar el webdriver de selenium
driver = webdriver.Firefox() #Segundo se crea un webdriver especifico para el navegador en este caso firefox
driver.get("https://google.com.ar") #Metodo get para indicarle que navege al sitio web que uno quiera
driver.quit() #Metodo para cerrar el navegador y el driver