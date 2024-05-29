from robocorp.tasks import task
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

from classes.News import News

import requests
import time
import os


URL = "https://apnews.com/"


@task
def main_task():
    with webdriver.Chrome() as driver:
        #Browser settings
        driver.implicitly_wait(10)
        driver.set_window_size(1024, 768)

        #Opening Browser and searching phrase
        driver.get(URL)    
        driver.find_element(By.XPATH, '/html/body/div[2]/bsp-header/div[2]/div[3]/bsp-search-overlay/button').click()
        driver.find_element(By.XPATH, '/html/body/div[2]/bsp-header/div[2]/div[3]/bsp-search-overlay/div/form/label/input').send_keys("COVID" + Keys.ENTER)
        
        #Selecting to newest news
        newest_news = driver.find_element(By.XPATH, '/html/body/div[3]/bsp-search-results-module/form/div[2]/div/bsp-search-filters/div/main/div[1]/div/div/div/label/select')
        select = Select(newest_news)
        select.select_by_value('3')

        var_strResponse = requests.get(URL)
        var_strResponse = var_strResponse.content

        #Get News
        news = News()
        news.get_news(var_strResponse)


