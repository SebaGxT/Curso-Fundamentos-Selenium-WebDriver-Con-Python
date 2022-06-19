import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC

class Page2:
    
    def __init__(self,driver):
        self.driver = driver
    
    def meterNombre(self,nombre):

        espera = WW(self.driver,10)
        nombre2 = espera.until(EC.element_to_be_clickable((By.ID,'Segundo')))
        if nombre2 is not None:
            nombre2.send_keys(nombre)
            time.sleep(3)
            print('Prueba exitosa')