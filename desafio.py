import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def buscarInformacoesEmpresa(nomeEmpresa, driver):
    driver.get("https://www.google.com/maps")
    time.sleep(2)

    campoBusca = driver.find_element(By.ID, "searchboxinput")
    campoBusca.clear()
    campoBusca.send_keys(nomeEmpresa)
    campoBusca.send_keys(Keys.RETURN)
    time.sleep(3)

    try:
        endereco = driver.find_element(By.CLASS_NAME, "Io6YTe").text
    except:
        endereco = "Não encontrado"

    try:
        rating = driver.find_element(By.CLASS_NAME, "MW4etd").text
    except:
        rating = "Não encontrado"

    return endereco, rating

def main():
    df = pd.read_excel("./Lista de Empresas.xlsx")

    driver = webdriver.Chrome()
    driver.get("https://www.google.com/maps")

    enderecos = []
    ratings = []

    for empresa in df["Nome da Empresa"]:
        endereco, rating = buscarInformacoesEmpresa(empresa, driver)
        enderecos.append(endereco)
        ratings.append(rating)

    df["endereco"] = enderecos
    df["Rating"] = ratings
    df.to_excel("dados.xlsx", index=False)
    driver.quit()

main()
