# find_element_by_name

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.clouditeducation.com/pruebas/index.html')

element = driver.find_element_by_name('tabla_prueba')

if element is not None:
    print('\nEl nombre: tabla_prueba fue encontrado\n')

driver.quit()