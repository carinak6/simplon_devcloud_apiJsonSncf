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
""" url = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
headers = {"Authorization": "e3f2b3a6-caa9-47d7-98ee-1f67379e654b"}
response = requests.get(url, headers=headers)
raw_data = json.loads(response.text) """
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
""" toutesArrets = raw_data['stop_areas'] """
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

#print(type(toutesArrets[0]['administrative_regions']))# <class 'list'>
#creer un fichier csv avec open et write
#je vais utiliser des list : en premier je cree les entete et apres le contenu

""" entetes =[u'id', u'Arret']
contenu =[]

for arret in toutesArrets:
    #print(type(arret))# <class 'dict'> 
    #bloque pour definir l'id
    local_id ='' 
    if type(arret) == dict:
        if "id" in arret.keys() : #len(arret['id'].strip()) != 0              
            local_id = arret['id']
            #list_ids.append(local_id)
            #print(local_id)
        else:
            #print('id inexistante')
            local_id ='id inexistante'
    else:
        #print(f'Format inconnu {type(arret)}')    
        local_id ='id inexistante'
    #print(local_id)

    #bloque de code pour avoir les label, le nom de l'arret
    local_label=''

    #if 'administrative_regions' in arret: #pour verifier quand on utilise l admintrative_regions
    if 'label' in arret.keys() and len(arret['label']) != 0 : #and arret['label'].isspace() == False: 
        #print('combien : ',len(arret['administrative_regions']), 'type : ',type(arret['administrative_regions']))#<class 'list'>
        #print("un arret administrative_regions name ==> ",arret['administrative_regions'][0]['name']) #['administrative_regions']
        
        #print("un arret name ==> ",arret['label'])
        local_label= arret['label']
    else:
        #print('Pas de administrative_regions')
        local_label= 'label inexistant'
    
    #print(local_label)

    contenu.append([local_id, local_label]) # je cree la liste avec les donnes pris pour chaque arret

#print(contenu) #verifie si la liste est bien crée """

""" fichierCSV = open('sncfPremier.csv', 'w') #je ouvre le fichier, il effacera les donnes anciennes
ligneEntete = ";".join(entetes) + "\n" # je tranforme les entetes en string separé par ';' et pour passer à l'autre '\n'
fichierCSV.write(ligneEntete)  #j ecris sur le fichier
for valeur in contenu: # je parcour la liste de contenu
     ligne = ";".join(valeur) + "\n" # pour chaque ligne on separe les valeurs par ';' et j'ajoute une retour à la ligne
     fichierCSV.write(ligne) # j ecrit la ligne sur le fichier
print('fichier csv cree!!')
fichierCSV.close() #je ferme le fichier pour liberer les ressources """

#TODO : il y a aussi un module CSV sur python pour travailler la creation des fichiers CSV
#les filles sont utilisé panda, à faire les deux option
#TODO : faire le CSV pour les url(links)

'''---- Récupérer les informations sur un trajet entre Paris Gare de Lyon et Lyon Perrache '''
#Paris - Gare de Lyon (code de la gare : stop_area:OCE:SA:87686006) 
#Lyon - Gare Lyon Perrache (code de la gare : stop_area:OCE:SA:87722025) 
url = "https://api.sncf.com/v1/coverage/sncf/journeys?from=stop_area:OCE:SA:87686006&to=stop_area:OCE:SA:87722025"
headers = {"Authorization": "e3f2b3a6-caa9-47d7-98ee-1f67379e654b"}
responseTrajetParisLyon = requests.get(url, headers=headers)
dataParisLyon = json.loads(responseTrajetParisLyon.text)
#pprint.pprint(dataParisLyon)
#print(type(dataParisLyon)) #<class 'dict'>
#print(dataParisLyon.keys()) #dict_keys(['tickets', 'links', 'journeys', 'disruptions', 'notes', 'feed_publishers', 'context', 'exceptions'])
#print(type(dataParisLyon['journeys'])) #<class 'list'>

#Informations sur le trajet : les vides sont notes, tickets, disruptions, exceptions et feed_publishers
#print(dataParisLyon['context'])
#print(dataParisLyon['context']['current_datetime']) #20210124T211113 date de la requete
#print(dataParisLyon['context']['car_direct_path']) #emision carbone du trajet {'co2_emission': {'value': 97091.1386812212, 'unit': 'gEC'}}

""" 
for valor in dataParisLyon['journeys']:
    print(type(valor)) #<class 'dict'>
    #print(valor.items())
    print(valor.keys()) 
    #dict_keys(['status', 'distances', 'links', 'tags', 'nb_transfers', 'durations', 'arrival_date_time', 'calendars', 'departure_date_time', 'requested_date_time', 'fare', 'co2_emission', 'type', 'duration', 'sections'])
"""

#code pour afficher tous les cles et types
journeys = dataParisLyon['journeys'][0]
"""for key in journeys :
    print(type(journeys[key]), key) """

#print(journeys.keys()) 
#dict_keys(['status', 'distances', 'links', 'tags', 'nb_transfers', 'durations', 'arrival_date_time', 'calendars', 'departure_date_time', 'requested_date_time', 'fare', 'co2_emission', 'type', 'duration', 'sections'])

#---- combien y a-t-il d’arrêts entre ces deux gares ? (utilisez la clé ‘journeys’)
#print(' Dans ce trajet il y a ', journeys['nb_transfers'], ' arrets' )

""" code que j'ai cree avant de savoir que nb_transfers represent les transfert, VOIR la DOC sncf, mais je laisse le code pour l utiliser apres
#print(type(journeys)) #<class 'list'>
#print(journeys)

#print(len(journeys)) #il y a 1 seule element
#varArrivalDateTime = journeys[0]["arrival_date_time"]# c est le date time general du trajet
#print(type(varArrivalDateTime)) # <class 'str'>
#print(len(varArrivalDateTime))  # il y a 15 cracteres
#print(varArrivalDateTime.keys())

nro_arret=0
time_sections=[] # pour calculer le temps d'arret de chaqu'une
#arrival_time = []
for loop_arrival_time in journeys: #(list) il y a un seule dans ce trajet
    #print(type(loop_arrival_time)) #<class 'dict'>
    #print(loop_arrival_time.keys())#dict_keys(['status', 'distances', 'links', 'tags', 'nb_transfers', 'durations', 'arrival_date_time', 'calendars', 'departure_date_time', 'requested_date_time', 'fare', 'co2_emission', 'type', 'duration', 'sections'])
    #print(loop_arrival_time["arrival_date_time"]) #date_time du trajet
    
    #print(type(loop_arrival_time['sections'])) # <class 'list'>
    #print(len(loop_arrival_time['sections'])) # il y a 3 sections
    nro_arret = len(loop_arrival_time['sections'])

    if type(loop_arrival_time['sections']) == list:

        for loop_section in loop_arrival_time['sections']: #date_time de chaque section
            #print(type(loop_section)) # <class 'dict'>
            #print(loop_section.keys()) # dict_keys(['from', 'links', 'arrival_date_time', 'co2_emission', 'to', 'departure_date_time', 'duration', 'type', 'id', 'mode'])
            #print(type(loop_section["to"])) #<class 'dict'>
            #print(loop_section["to"].keys()) # dict_keys(['embedded_type', 'stop_point', 'quality', 'name', 'id'])

            #je sais pas si je comprends bien d'une section le time d arrivé c est le temps 
            temps_arrive= loop_section["arrival_date_time"]
            temps_depart = loop_section["departure_date_time"]

            temps_conv_arrive = parser.parse(temps_arrive)
            temps_conv_depart = parser.parse(temps_depart)
            #print(type(temps_conv_depart)) #<class 'datetime.datetime'>

            temps_conv_arrive2 = temps_conv_arrive.strftime("%b %d %Y %H:%M:%S") #'Jan 25 2021 05:52:00'
            temps_conv_depart2 = temps_conv_depart.strftime("%b %d %Y %H:%M:%S")

            #print(temps_conv_depart)

            #deFrom = loop_section["from"]['name']
            #aTo = loop_section["to"]['name']
            #affichage_direction = loop_section["display_informations"]
            dureSection = loop_section['duration']
            idSection = loop_section['id']
            #print("section ==> ",loop_section["arrival_date_time"])
            time_sections.append([idSection,temps_conv_depart2, temps_conv_arrive2, dureSection])
            #arrival_time.append(loop_section["arrival_date_time"])

"""
sections = journeys['sections'] #list
#print(sections[1]) #celui-la à les arret dans stop_date_time

sectionArrets = sections[1]
#print(len(sectionArret['stop_date_times']))
#print(type(sectionArrets)) # <class 'dict'>
nb_arrets = len(sectionArrets['stop_date_times']) - 2 #parce qu il y a le depart et arrive inclue aussi
list_arrets=[]
temps_arrets=[]

for cle, stop in enumerate(sectionArrets['stop_date_times']):#<class 'dict'>
    #print(type(stop))#<class 'dict'>
    #print(stop['stop_point'])#dict
    #print(stop['stop_point']['name'])
    #print(cle)
    if cle != 0 and cle != (len(sectionArrets['stop_date_times']) -1):
        list_arrets.append(stop['stop_point']['name'])
        
        #je sais pas si je comprends bien d'une section le time d arrivé c est le temps 
        temps_arrive= stop["arrival_date_time"]
        temps_depart = stop["departure_date_time"]

        temps_conv_arrive = parser.parse(temps_arrive)
        temps_conv_depart = parser.parse(temps_depart)
        #print(type(temps_conv_depart)) #<class 'datetime.datetime'>

        temps_conv_arrive2 = temps_conv_arrive.strftime("%b %d %Y %H:%M:%S") #'Jan 25 2021 05:52:00'
        temps_conv_depart2 = temps_conv_depart.strftime("%b %d %Y %H:%M:%S")

        #print(temps_conv_depart)
        #temps_arrets.append([stop['arrival_date_time'],stop['departure_date_time']])
        temps_arrets.append([temps_conv_arrive2,temps_conv_depart2 ])

print('Dans ce trajet il y a ', nb_arrets, ' arrets : ',list_arrets)



#---- combien de temps d’arrêt à chacune d’elles ?

#print("Temps entre les arrets est ", journeys['durations']['total'])
print("Temps entre les arrets est ", temps_arrets)

#print('Le temps d’arrêt à chacune d’elles : ', time_sections)
""" for section_affic in time_sections:
    print("Section ", section_affic[0]," depart : ", section_affic[1] , " arrive : ", section_affic[2]) """


#---- Vous êtes Gare de Lyon et il est 18h00. Combien de tgv partent entre 18h00 et 20h00 ?

#https://api.navitia.io/v1/journeys?from={resource_id_1}&to={resource_id_2}&datetime={date_time_to_leave}
""" date_time_to_leave = datetime.n
url = "https://api.sncf.com/v1/coverage/sncf/journeys?from=stop_area:OCE:SA:87686006&to=stop_area:OCE:SA:87722025&datetime={date_time_to_leave}"
headers = {"Authorization": "e3f2b3a6-caa9-47d7-98ee-1f67379e654b"}
responseTrajetParisLyon = requests.get(url, headers=headers)
dataParisLyon = json.loads(responseTrajetParisLyon.text) """

#---- Lequel arrive le plus tôt à sa destination finale ?

#---- Essayer de trouver toutes les correspondances possibles depuis un trajet entre Paris et Perpignan

#---- Transformer une ou plusierus des donneess renvoyes par lapi en une ou plusieurs tables CSV

#---- Bonus: Représenter toutes les gares atteignables avec un graphique type scatter.
#---- Distinguer les gares atteintes en un seul trajet et celles atteintes avec une correspondance.

#print("date_timme de chaque section ",arrival_time)
