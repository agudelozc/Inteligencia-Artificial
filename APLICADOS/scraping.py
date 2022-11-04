from requests import get
import time
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
while(False):
    time.sleep(10)
    website = 'https://www.kitco.com/charts/livegold.html'
    response = get(website)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)
    oro = html_soup.find(id='sp-bid')
   #print(golden.get_text())
    oro = (oro.get_text())
    fecha = datetime.now()
    oro = oro.replace(",",".")
    print(oro)
    with open("dataoro.csv","a") as archivo:
        archivo.write(oro)
        archivo.write(",")
        archivo.write(str(fecha))
        archivo.write("\n")
        archivo.close()
#sp-bid
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
while(True):
        time.sleep(10)
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get("https://www.kitco.com/charts/livegold.html")
        datos = driver.find_element_by_id("sp-chg-value").text
        print(datos)
        fecha = datetime.now()
        with open("procentaje.csv","a") as archivo:
         archivo.write(datos)
         archivo.write(",")
         archivo.write(str(fecha))
         archivo.write("\n")
         archivo.close()
         #cerrar ventana de firefox
         driver.close()