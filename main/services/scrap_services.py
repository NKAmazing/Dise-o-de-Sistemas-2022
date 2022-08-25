from re import search


from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import os 

class ScrapServices:
    def __get_services(self):
        service = Service(log_path=os.path.devnull)
        return service

    def __get_options(self):
        options = webdriver.FirefoxOptions()
        options.headless = True
        options.set_preference("browser.cache.disk.enable", False)
        options.set_preference("browser.cache.memory.enable", False)
        options.set_preference("browser.cache.offline.enable", False)
        options.set_preference("network.http.use-cache", False)
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.log.level = "INFO"
        return options

    def __get_browser(self):
        browser = webdriver.Firefox(options=self._get_options(), service=self._get_services())
        browser.set_window_position(0, 0)
        return browser

    def search(self, keyword:str):
        #TODO: buscar en el sitio codigofacilito devoler html 
        browser = self.__get_browser()
        browser.get("https://codigofacilito.com/search?keyword=python")
        
    def save_data(self, datalist):
        #TODO: guardar los 
        pass
    def parser(self, html:str):
        #TODO: 
        pass
