#TODO: crear resource con blue_print
from flask import Blueprint
from main.services import ScrapServices

scrapblue = Blueprint('scrapblue',__name__)

@scrapblue.route('/search/<keyword>/', methods=['GET'])
def search(keyword:str):
    scrap_service = ScrapServices()
    scrap_service.search("python")