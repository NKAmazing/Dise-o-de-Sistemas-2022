from .browser_firefox import BrowserFirefox
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from main.models import CourseModel

class ScrapServices:

    def __init__(self):
        self.browser_firefox = BrowserFirefox()

    def search(self, keyword:str):
        html = self.browser_firefox.search(keyword)
        self.parser(html)

    def save_data(self, datalist):
        #TODO: guardar los 
        pass

    def parser(self, html:WebDriver):
        course_search = html.find_element(By.ID,
                                'courses_search')

        if course_search != None:
            list_courses = course_search.find_elements(By.CLASS_NAME,
                                    'pointer')
            for card_course in list_courses:
                #TODO: Hacer lista de la clase cursos y ir agregando.
                #course = CourseModel()
                href = card_course.get_attribute("href")
                if href != None:
                    #course.url(href)
                    title = card_course.find_element(By.CLASS_NAME, "h5")
                    print(title.text)
