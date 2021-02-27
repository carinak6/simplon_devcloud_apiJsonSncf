"""
 https://api.sncf.com/v1/coverage/sncf/journeys?from=admin:7444extern&to=admin:120965extern&datetime=20170123T140151

Repondez aux questions suivantes dans un script python que vous mettrez sur github.

******** manipuler un json dans python: **********
"""
#importation des librairies
import pprint
import json
import requests
import datetime
from dateutil import parser
import time

#url = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
#url = "https://api.sncf.com/v1/coverage/sncf/journeys?from=stop_area:OCE:SA:87686006&to=stop_area:OCE:SA:87722025"



"""  TIPHAINE
    def write_json(self, file_name):#crée mon fichier json uniquement de mes "stop_areas"
        self.url_request = requests.get(url = self.URL, headers= self.headers)
        with open(file_name, mode = "w") as file : #mon nom de fichie est "stop_areas_tiph.json"
            json.dump(self.url_request.json(), file)
            #retourne rien, juste pour sauvegarder le json

 #   def_write_json = write_json()

    def read_links(self, file_name): # enregistre mes liens 
        with open(file_name) as json_stop_areas_file: #"stop_areas_tiph.json"
            self.raw = json.load(json_stop_areas_file) """ 



class Sncf():

    def __init__(self):
        self.url = "https://api.sncf.com/v1/coverage/sncf/"
        self.headers = {"Authorization": "e3f2b3a6-caa9-47d7-98ee-1f67379e654b"}
        self.fileJson="jsonReponse3" #on l'ajoute l'extension apres dans les methodes
        self.contenuJson = []

#requete represente la partie variable de l'url sncf
    def readJson(self, requete):
        print(self.url+requete)
        response = requests.get(self.url+requete, headers=self.headers)          
        with open(self.fileJson+".json", mode="w") as file:
            json.dump(response.json(), file)

        #return raw_data #<class 'dict'>

    def getJson(self):

        with open(self.fileJson+'.json') as json_stop_journey: #"stop_areas_tiph.json"
            self.contenuJson = json.load(json_stop_journey)
        
        return self.contenuJson #mettre dans un attribute et rien retourné, a voir!!


    #combien y a-t-il d’arrêts entre ces deux gares ?
    def combien_arrets(self, requete):
        self.readJson(requete)
        fichierJson = self.getJson()
        journeys = fichierJson['journeys'][0]
        sections = journeys['sections'] #list
        sectionArrets = sections[1] # la section 1 contient tous les donnes
        nb_arrets = len(sectionArrets['stop_date_times']) - 2

        return nb_arrets
    

    

    