from .browser_firefox import BrowserFirefox

class ScrapServices:

    def __init__(self):
        self.browser_firefox = BrowserFirefox()

    def search(self, keyword:str):
        self.browser_firefox.search(keyword)

    def save_data(self, datalist):
        #TODO: guardar los 
        pass

    def parser(self, html):
        pass
