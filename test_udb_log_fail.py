import pytest
import time
from selenium import webdriver
from allure_commons.types import AttachmentType
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
driver=""

#pagina de login
#ingreso de sitio web,agrandamiento de pantalla y mas tiempo de espera
@pytest.mark.notrun
def test_uno():
    driver = webdriver.Chrome()
    driver.get("https://www.udbvirtual.edu.sv/auladigital/login/index.php")
    driver.maximize_window()
    driver.implicitly_wait(10)
    time.sleep(2)

#validacion de titulo de pagina
    driver.get("https://www.udbvirtual.edu.sv/auladigital/login/index.php")
    try:
        assert "Aula Digital: Entrar al sitio" == driver.title
        print("Prueba exitosa: El título de la página es correcto.")
    except AssertionError:
        print("Prueba fallida: El título de la página no coincide.")

#colocar username correcto pero password incorrecto y validar el mensaje de error
    usuario = driver.find_element(By.XPATH, "//input[@id='username']")
    usuario.send_keys("VP223250")
    time.sleep(2)
    contr = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
    contr.send_keys("sahdahsdha")
    time.sleep(2)
    botn = driver.find_element(By.XPATH, "//button[contains(@id,'loginbtn')]")
    botn.click()
    time.sleep(2)

    inva = driver.find_element(By.XPATH, "//div[@class='alert alert-danger'][contains(.,'Acceso inválido. Por favor, inténtelo otra vez.')]")
    if(inva.is_displayed() == True):
        print("El mensaje de acceso invalido esta visible")
    else:
        print("El mensaje de acceso invalido no esta visible")

    time.sleep(2)
    driver.quit()

#pagina de login
@pytest.mark.notrun
def test_dos():
    driver = webdriver.Chrome()
    driver.get("https://www.udbvirtual.edu.sv/auladigital/login/index.php")
    driver.maximize_window()
    driver.implicitly_wait(10)
    time.sleep(2)

# validacion de titulo de pagina
    driver.get("https://www.udbvirtual.edu.sv/auladigital/login/index.php")
    try:
        assert "Aula Digital: Entrar al sitio" == driver.title
        print("Prueba exitosa: El título de la página es correcto.")
    except AssertionError:
        print("Prueba fallida: El título de la página no coincide.")

#Se va a la seccion de informacion que esta en la parte baja y luego se valida que este visible y completa la seccion
    driver.execute_script("window.scrollTo(0,500)")
    time.sleep(2)

    info = driver.find_element(By.CLASS_NAME, "col-md-3")
    if(info.is_displayed() == True):
        print("La seccion de informacion esta visible")
    else:
        print("La seccion de infomacion no esta visible")
        time.sleep(2)

#estando ya en la parte baja se valida que este visible y completa la seccion de contactanos
    contac = driver.find_element(By.XPATH, "//h5[@class='nopadding'][contains(.,'Contáctanos')]")
    if(contac.is_displayed() == True):
        print("La seccion de contactanos esta visible")
    else:
        print("La seccion de contactanos no esta visible")
        time.sleep(2)

#estando ya en la parte baja se valida que este visible y completa el unico simbolo de redes sociales (facebook)
    rsociales = driver.find_element(By.XPATH, "//i[contains(@class,'fa fa-facebook-square')]")
    if(rsociales.is_displayed()  == True):
        print("El simbolo de redes sociales de facebook esta visible")
    else:
        print("El simbolo de redes sociales de facebook no esta visible")
        driver.quit()



#pagina principal udb, pero primero se introduciran los datos correctos de usuario y password
# se esta en la pagina principal de udb
@pytest.mark.run
def test_tres():
    driver = webdriver.Chrome()
    driver.get("https://www.udbvirtual.edu.sv/auladigital/login/index.php")
    driver.maximize_window()
    driver.implicitly_wait(10)
    # validando titulo de pagina y mostrando en consola opcion2
    titulo_pagina = driver.title
    print("El título de la página es:", titulo_pagina)
    assert titulo_pagina == "Aula Digital: Entrar al sitio", "El título no es el esperado"
    time.sleep(2)

    #validando titulo de pagina y pero no muestra en consola opcion1
    #titulo_pagina = driver.title
    #assert titulo_pagina == "Aula Digital: Entrar al sitio"

    #introduciendo los datos de usuario correctos
    usr = driver.find_element(By.XPATH, "//input[@id='username']").send_keys("VP223250")
    passw = driver.find_element(By.XPATH, "//input[contains(@id,'password')]").send_keys("Metalero97")
    btn = driver.find_element(By.XPATH, "//button[contains(@id,'loginbtn')]").click()
    time.sleep(2)

    #entramo al menu principal del portal educativo y cerramos session
    logout_button = driver.find_element(By.XPATH, "//a[@href='#'][contains(.,'Roger Eduardo Vásquez Portillo')]")
    logout_button.click()
    logout_button = driver.find_element(By.XPATH, "//span[contains(@id,'actionmenuaction-7')]")
    logout_button.click()
    wait = WebDriverWait(driver, 10)
    try:
        # Espera hasta que el elemento que indica que la sesión ha sido cerrada aparezca
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-success'][contains(.,'Si eres estudiante de pregrado o postgrado utiliza las mismas credenciales del Portal Web. Si tienes problemas de acceso verifica que tu contraseña contenga solo letras y números.')]")))
        print("Te has deslogeado del portal educativo con éxito.")
    except TimeoutException:
        print("Error: No te has deslogeado del portal educativo.")
    time.sleep(2)
    driver.quit()



