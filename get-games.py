import requests
from bs4 import BeautifulSoup
import config
import sys
import json
import re


def get_list_of_games():
    r = requests.get(config.url)
    soup = BeautifulSoup(r.content, features="lxml")
    data = soup.find('script', language='javascript').text

    # Finds the javascript variable with the game data in
    regex = re.compile('var ' + config.javascript_var_name + ' = (.*?);')
    jsonData = regex.search(data)

    # Loads it into a json object but strips off the variable declaration stuff
    games = json.loads(
        jsonData.group()[(len('var ' + config.javascript_var_name + ' = ')):-1])

    for game in games:
        print(game)


get_list_of_games()
