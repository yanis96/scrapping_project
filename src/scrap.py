import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import requests
import json


class Scrap:

    #Constructeur
    def __init__(self, path):
        self.driver = webdriver.Chrome(path)

    #Ouvrir le navigateur et naviguer vers le l'url su site passé en paramètre
    def go_to_web_site(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        return True

    #Fermer les cookies du site
    def close_cookie(self, element_xpath):
        cookie = self.driver.find_element_by_xpath(element_xpath)
        cookie.click()
        return True

    #Stoper le processus temporairement en fonctions des secondes passées en paramètre
    def sleep(self, sec):
        time.sleep(sec)
        return True

    #Clicker sur un element clickable sur site
    def click_element(self,element_xpath):
        page = self.driver.find_element_by_xpath(element_xpath)
        page.click()
        return True

    #Scroller jusqu'a
    def scroll_to_element(self, element_xpath):
        element = self.driver.find_element_by_xpath(element_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        return True

    #Récuperer une listes d'elements
    def get_list_info(self, elemets_xpath):
        list_info = self.driver.find_elements_by_xpath(elemets_xpath)
        return list_info


    #Fermer le navigateur
    def close_browser(self):
        self.driver.close()

    def to_dataFrame(self,element,col):
        df = pd.DataFrame(element,columns=col)
        return df
