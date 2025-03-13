from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 

navegador=webdriver.Chrome()

navegador.get('https://www.municipioonline.com.br/rn/prefeitura/serrinhadospintos/contribuinte/notafiscal/login')
navegador.maximize_window()
time.sleep(2)

navegador.find_element('id', 'body_txtContribuinte').send_keys('37108399000139')
navegador.find_element('id', 'body_txtUser').send_keys('03387483422')
navegador.find_element('id', 'body_txtPassword').send_keys('12345678')

time.sleep(2)

navegador.find_element('id', 'body_btnEntrar').click()
time.sleep(2)
navegador.find_element('id', 'tabRelatorio').click()
time.sleep(2)
select=Select(navegador.find_element('id','ddlmesComp'))
select.select_by_visible_text('Fevereiro')
time.sleep(2)
navegador.find_element('id', 'btnImpRelNota').click()
time.sleep(5)

#iframe 
navegador.switch_to.frame('iframeRelatorio')

shadow_host = navegador.find_element(By.TAG_NAME, "cr-icon-button")
shadow_root = navegador.execute_script("return arguments[0].shadowRoot", shadow_host)
download_button = shadow_root.find_element(By.ID, "download")

navegador.execute_script("arguments[0].click();", download_button)

time.sleep(5)
navegador.switch_to.default_content()


# 37.108.399/0001-39
# 033.874.834-22
# 12345678