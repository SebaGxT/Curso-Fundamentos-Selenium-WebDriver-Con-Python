# find_element_by_id

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.clouditeducation.com/pruebas/index.html')

element = driver.find_element_by_id('noImportante')

if element is not None:
    print('\nElemento noImportante encontrado\n')

driver.quit()