"""
 https://api.sncf.com/v1/coverage/sncf/journeys?from=admin:7444extern&to=admin:120965extern&datetime=20170123T140151

Repondez aux questions suivantes dans un script python que vous mettrez sur github.

******** manipuler un json dans python: **********
"""
#importation des librairies
import pprint
import json
import requests

#----lisez le fichier json joint a ce brief (stop_areas.json), pour l'adresse du fichier je puet mettre avec ./ ou sans ça
#le fichier stop_areas est bien un json
""" json_data = None
f= open("./stop_areas.json","r")
backup_liste = f.read() """
#print('type ',type(backup_liste), backup_liste) #type  <class 'str'> et il retourne bien des donnes

""" json_data = json.loads(backup_liste) """#la methode loads prends une chaîne JSON ici un str, pour l'analyser et return un dict
#print(type(json_data)) #return <class 'dict'>
#print(json_data)

#une autre maniere de afficher correctement un json
#json_formatted_str = json.dumps(json_data, indent=2)
#print(json_formatted_str)

#----afficher le avec le module prettyprint
#pprint.pprint(obj) Imprime la représentation formatée de l' objet sur le flux
#pprint.pprint(json_data) #il affiche correctement le json, il reemplace le print(), on peut reaffecter son retour a une variable
                        # et on pourra traiter la taille et autres choses

#----rajouter un arret dans le json (utiliser dump ou dumps)
#dumps : Si vous avez un objet Python, vous pouvez le convertir en chaîne JSON à l'aide de la méthode json.dumps().
#convert into JSON, the result is a JSON string
""" chaineJson = json.dumps(json_data)  """
#print('type ', type(chaineJson))#il retourn type  <class 'str'>
#print('valeur', chaineJson)

""" jsonStopAreas = json_data['stop_areas'] """
#print(jsonStopAreas[0]) pour verifier
#print(type(jsonStopAreas)) #<class 'list'>

#je cree une nouvelle arret
""" nouvelleArret = {'codes': [{'type': 'EPI-SUR-SEI', 'value': '93800-BV'}], 'name': 'Epinay Sur Seine - Les Econdeaux', 'links': [], 'coord': {'lat': '49.24065', 'lon': '6.990968'}, 'label': 'Epinay Sur Seine (Les Econdeaux)', 'timezone': 'Europe/Paris', 'id': 'stop_area:OCE:SA:12393800'} """
#j'ajoute une nouvelle arret à stop_areas, avec append dans le dict
""" json_data['stop_areas'].append(nouvelleArret) """
#print(json_data['stop_areas'])
'''
----requeter une api
-----renseignez vous sur les differents endpoints (qu'est ce que c'est?)
Un Endpoint est ce qu’on appelle une extrémité d’un canal de communication, lorsqu’une API interagit avec un autre système,
les points de contact de cette communication sont considérés comme des Endpoints.
C'est l’emplacement à partir duquel les API peuvent accéder aux ressources dont elles ont besoin pour exécuter leur fonction
un Endpoint représente l’endroit où les API envoient les demandes et où réside la ressource

----lire le json donnee par le endpoint https://api.sncf.com/v1/coverage/sncf/stop_areas (utilisez requests)'''
#ça marche
url = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
headers = {"Authorization": "e3f2b3a6-caa9-47d7-98ee-1f67379e654b"}
response = requests.get(url, headers=headers)
raw_data = json.loads(response.text)
#print(raw_data)

'''
---- Trouver l’ensemble des gares disponibles sur l’API '''

#for key in raw_data:
#    print(key,' -> ',raw_data[key])

#raw_data_items = raw_data.items() #on affiche les valeurs d un dict
#print(raw_data_items)

""" for item in raw_data_items:
    print(item) """

""" for value in raw_data: #on affiche les index
    print(value) #return âgination, links, disruptions, stop_areas, etc """

""" for key,value in raw_data.items():
    print(f"{key} is {value}") """


#print(raw_data.keys()) #dict_keys(['pagination', 'links', 'disruptions', 'feed_publishers', 'context', 'stop_areas'])
toutesArrets = raw_data['stop_areas']
#print(type(toutesArrets)) #<class 'list'>
#print(type(toutesArrets[0])) #<class 'dict'>

#on parcours une liste de toutes les arret et j'affiche le nom de chaque
""" for arret in toutesArrets:
    #print(type(arret))# <class 'list'> verifier
    print(arret['label']) """
""" list_ids =[]
for loop_area in toutesArrets:
    if type(loop_area) == dict:
        if "id" in loop_area.keys():
            local_id = loop_area['id']
            list_ids.append(local_id)
        else:
            print('id inexistante')
    else:
        print(f'Format inconnu {type(loop_area)}')
print('Combien des id on trouve ',len(list_ids), list_ids)"""

'''
faire le meme avec les links

'''
""" tousLinks = raw_data['links']
#print(type(tousLinks), tousLinks) #<class 'list'>
print("Les differents point d entre de l'api")
print("On trouve "+str(len(tousLinks))+" points d'entres")
for urlapi in tousLinks:
    print(urlapi['href']) """

'''
---- et créer un fichier csv avec les codes de la gare, son nom et ses coordonnées latitude et longitude,
ainsi que les informations administratives de la région quand elles sont disponibles
'''

 print(type(toutesArrets[0]['administrative_regions']))# <class 'list'>

for arret in toutesArrets:
    #print(type(arret))# <class 'dict'>   
   
    if 'administrative_regions' in arret: 
        print('combien : ',len(arret['administrative_regions']), 'type : ',type(arret['administrative_regions']))
        print("un arret ==> ",arret['administrative_regions']) #[0]['name']) #['administrative_regions']
    else:
        print('Pas de administrative_regions')

'''---- Récupérer les informations sur un trajet entre Paris Gare de Lyon et Lyon Perrache '''