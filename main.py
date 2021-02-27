import pprint
from sncf import Sncf

def main():
    #apres je decompeserai les choix de l utilisateur

    #type de requete
    typeRecherche="TGV"

    #partie choisir les villes del trajet
    #faire une function qui retourne les links, les journey

    def choisirVillesDepart():
        #afficher des options et que le utilisateur choissira
        #depuis le process du choix on affiche son code correspondant
        ville = "stop_area:OCE:SA:87686006" #exemple
        return ville

    def choisirVillesArrivee():
        #afficher des options et que le utilisateur choissir
        ville = "stop_area:OCE:SA:87722025" #exemple
        return ville

    obj_recherche=""

    quoiFaire=""

    if typeRecherche =="Gares Disponible":
        quoiFaire ="/stop_areas"

    elif typeRecherche== "trajet":
        
        ville_depart=choisirVillesDepart()
        ville_arrivee= choisirVillesArrivee()
        quoiFaire = "journeys?from="+ville_depart+"&to="+ville_arrivee

    elif typeRecherche == "TGV":
        ville_depart=choisirVillesDepart()
        quoiFaire = "physical_modes/physical_mode:LongDistanceTrain/stop_areas/"+ville_depart+"/departures?from_datetime=20210131T150000"

    
    #il faudra avoir une maniere d afficher les villes et apres remplir le code correpondant pour faire la requete

    print(quoiFaire)
    objClass = Sncf()
    objClass.readJson(quoiFaire)
    fichierRecupere= objClass.getJson()
    #pprint.pprint(fichierRecupere)
    print(type(fichierRecupere) == dict) #<class 'dict'>



if __name__ == '__main__':
    main()