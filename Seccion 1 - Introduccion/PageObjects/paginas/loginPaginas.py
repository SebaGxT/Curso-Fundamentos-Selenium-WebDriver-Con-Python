import time
from selenium.webdriver.common.by import By

class LoginPage:
   
    def __init__(self,driver):
        self.driver = driver
    
    def login(self,username,password):

        nombre = self.driver.find_element(By.ID,'nombre')
        if nombre is not None:
            nombre.send_keys(username)
            time.sleep(2)
        
        contra = self.driver.find_element(By.NAME,'contrasena')
        if contra is not None:
            contra.send_keys(password)
            time.sleep(2)

        login = self.driver.find_element(By.ID,'proceed')
        if login is not None:
            login.click()
            time.sleep(2)
            self.driver.get('https://www.clouditeducation.com/pruebas/nuevaPagina.html')