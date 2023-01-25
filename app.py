'''
    ConcursosNoBrasil web scrapper and API
'''

import string
import requests
from bs4 import BeautifulSoup
from flask import Flask, abort, jsonify

app = Flask(__name__)
availableCategories = ['br', 'ac', 'al', 'am', 'ap', 'ba', 'ce', 'df', 'es', 'go', 'ma', 'mg',
                       'ms', 'mt', 'pa', 'pb', 'pe', 'pi', 'pr', 'rj', 'rn', 'ro', 'rr', 'rs', 'sc', 'se', 'sp', 'to']
baseURL = 'https://concursosnobrasil.com/concursos/'
errorMessage = ''

def pageRequest(url: string):
    try:
        return requests.get(url)
    except requests.HTTPError:
        print("An http error has ocurred, process has exited")
        return None
    except:
        print("An error has ocurred, process has exited")
        return None


def initWebScraper(url: string, parser: string = 'html.parser'):
    webResponse = pageRequest(url)

    if(webResponse == None):
        print("Canceling scrapping")
        return None

    return BeautifulSoup(webResponse.content, parser)


def categoryTarget(category: string) -> None:
    global errorMessage 
    if ((len(category) != 2) or (category not in availableCategories)):
        errorMessage = "Invalid Category"
        return None

    return baseURL + category


def getCategoryItemStatus(item) -> string:
    try:
        item.find('span', class_='label-previsto').text
    except:
        return 'open'

    return 'expected'

@app.route('/')
def Greetings():
    return 'Hello! The API is Alive'


@app.route('/concursos/<categorySelect>', methods=['GET'])
def Concursos(categorySelect):
    concursosAvailable = []
    pageScraper = initWebScraper(categoryTarget(categorySelect))

    if(pageScraper == None):
        print("Developer: This is a security issue, do not propagate None result")
        abort(jsonify(message=errorMessage, code=400))


    availableItemsInCategory = pageScraper.find(
        'div', class_='list-concursos').find('tbody').find_all('tr')
    # analyzing contents

    for item in availableItemsInCategory:
        concursosAvailable.append({
            'organization': item.find('a').text.rstrip(),
            'workPlacesAvailable': item.find_all('td')[1].text.rstrip(),
            'link': item.find('a').get('href'),
            'status': getCategoryItemStatus(item)
        })

    #print(concursosAvailable)
    return jsonify(concursosAvailable)

#TODO: add an limitor factor for page access