#!/usr/bin/python3
# KUCUKSULLU Isra & FATHALLAH Mariam
# INM-02


from utils import db
from prettytable import PrettyTable
import sqlite3



def menu(conn):
    """
    Menu principal de l'interface.
    On revient à ce menu à chaque fois que l'on fait une action avec la DB.

    Prend en paramètre une connexion à la DB
    Ne renvoie rien.
    """

    print("\n=============" + "\33[7m" + " MENU " +
          "\33[0m" + "===============" + "\33[1m")
    print("""1. Insérer         4. Modifier
2. Supprimer       5. Sauvegarder
3. Afficher        6. Quitter  """)
    print("\33[0m" + "==================================")

    print("\nNB : N'oubliez pas de sauvegarder après avoir fait des modifications !!\n")

    while (True):
        try:
            action = int(input("\nEntrez le numéro de l'action que vous voulez effectuer : "))
        except ValueError:
            print("Entrée invalide : veuillez entrer un numéro.")
            continue        
        
        if action == 1:
            MenuInserer(conn)
        elif action == 2:
            MenuSupprimer(conn)
        elif action == 3:
            MenuAfficher(conn)
        elif action == 4:
            MenuModifier(conn)
        elif action == 5:
            conn.commit()
            print("\n\33[32m" + "Success!" + "\33[0m" +
                  " Changements sauvegardés !")
        elif action == 6:
            quit()
        else:
            print("Action inconnue...")    



def MenuInserer(conn):
    """
    Menu d'insertion.
    Permet d'insérer des données dans différentes tables à l'aide d'un numéro de choix.

    Prend en paramètre une connexion à la DB.
    Ne renvoie rien.
    """
    print("\n============" + "\33[7m" +
          " MENU D'INSERTION " + "\33[0m" + "===========")
    print("1. Insérer un Service")
    print("2. Insérer un membre au Personnel")
    print("3. Insérer un Patient")
    print("4. Insérer un couple Personnel-Patient")
    print()
    print("r : Retour au menu")
    print("q : Quitter")
    print("=========================================\n")

    while (True):
        choix = input("Entrez votre choix : ")
        choix_str = str(choix).strip()

        if choix_str.upper() == "R":
            menu(conn)
            return
        elif choix_str.upper() == "Q":
            quit()

        try:
            choix_int = int(choix_str)
        except ValueError:
            print("Entrée invalide : veuillez entrer un numéro, R ou Q.")
            continue

        if choix_int  == 1:
            insert_service(conn)
        elif choix_int  == 2:
            insert_personnel(conn)
        elif choix_int  == 3:
            insert_patient(conn)
        elif choix_int  == 4:
            insert_personnelpatient(conn)
        else:
            print("Numéro de choix inconnu...")



def MenuSupprimer(conn):
    """
    Menu de suppression.
    Permet de supprimer différentes relations (ou tables/vues) à l'aide d'un numéro de choix.
    Le choix est volontairement limité à cause de toutes les références entre les attributs.

    Prend en paramètre une connexion à la DB.
    Ne renvoie rien.
    """
    print("\n===========" + "\33[7m" +
          " MENU DE SUPPRESSION " + "\33[0m" + "==========")
    print("1. Supprimer une consultation")
    print("2. Supprimer un service")
    print("3. Supprimer toutes les tables")
    print()
    print("r : Retour au menu")
    print("q : Quitter")
    print("==========================================\n")
    while True:
        choix = input("Insérez un choix : ")

        choix_str = str(choix).strip()

        if choix_str.upper() == "R":
            menu(conn)
            return
        elif choix_str.upper() == "Q":
            quit()

        try:
            choix_int = int(choix_str)
        except ValueError:
            print("Entrée invalide : veuillez entrer un numéro, R ou Q.")
            continue

        if choix_int == 1:
            delete_from_consultations(conn)
        elif choix_int == 2:
            delete_from_services(conn)
        elif choix_int == 3:
            drop_all_tables(conn)
        else:
            print("Numéro de choix inconnu...")




def MenuAfficher(conn):
    """
    Menu d'affichage.
    Permet d'afficher différentes tables à l'aide d'un numéro de choix.

    Prend en paramètre une connexion à la DB.
    Ne renvoie rien.
    """
    print("\n============" + "\33[7m" +
          " MENU D'AFFICHAGE " + "\33[0m" + "===========")
    print()
    print("1. Afficher tous les Patients")
    print("2. Afficher tous les Patients ayant la grippe")
    print("3. Afficher les patients ayant une certaine maladie")
    print("4. Afficher tout le Personnel")
    print("5. Afficher tous les Médecins")
    print("6. Afficher toutes les Maladies")
    print("7. Afficher toutes les Consultations")
    print("8. Afficher les Patients qui sont venus plus d'une fois")
    print("9. Afficher tous les couples Personnel-Patient")
    print("10. Afficher les Services dans lesquels sont les patients")
    print("11. Afficher les Maladies qu'ont chacun des patients, avec leur gravité")
    print("12. Afficher les ensembles Services-Maladies")
    print("13. Afficher tous les Services")
    print("14. Aficher le nombre de patients qui utilisent un certain service")
    print("15. Afficher la liste du personnel qui n'a effectué aucune consultation")
    print()
    print("r : Retour au menu")
    print("q : Quitter")
    print()
    print("=========================================")


    choix = input("\nInsérez un choix : ")
    print()
    choix_str = str(choix).strip()

    if choix_str.upper() == "R":
        menu(conn)
        return
    elif choix_str.upper() == "Q":
        quit()

    try:
        choix_int = int(choix_str)
    except ValueError:
        print("Entrée invalide : veuillez entrer un numéro, R ou Q.")
        menu(conn)
        return

    if choix_int == 1:
        select_tous_les_patients(conn)
    elif choix_int == 2:
        select_patients_ayant_grippe(conn)
    elif choix_int == 3:
        select_patients_ayant_maladie(conn)  
    elif choix_int == 4:
        select_tout_le_personnel(conn)
    elif choix_int == 5:
        select_tous_les_medecins(conn)
    elif choix_int == 6:
        select_toutes_les_maladies(conn)
    elif choix_int == 7:
        select_toutes_les_consultations(conn)
    elif choix_int == 8:
        select_patients_abonnes(conn)
    elif choix_int == 9:
        select_personnel_patients(conn)
    elif choix_int == 10:
        select_patient_service(conn)
    elif choix_int == 11:
        select_patient_maladie(conn)
    elif choix_int == 12:
        select_service_maladie(conn)
    elif choix_int == 13:
        select_tous_les_services(conn)  
    elif choix_int == 14:
        select_utilisation_services(conn)
    elif choix_int == 15:
        select_personnel_nonConsultations(conn)
    else:
        print("Numéro de choix inconnu...")
            
    menu(conn)
    return




def MenuModifier(conn):
    """
    Menu de modification
    Permet de modifier certains attributs à l'aide d'un numéro de choix.
    Même remarque que pour la suppression, les options sont volontairement limitées
    à cause des références entre les attributs.

    Prend en paramètre une connexion à la DB.
    Ne renvoie rien.
    """
    print("\n============" + "\33[7m" +
          " MENU DE MODIFICATION " + "\33[0m" + "===========")
    print("1. Augmenter les frais de consultation de 20%")
    print("2. Modifier le service dans lequel travaille un membre du personnel")
    print()
    print("r : Retour au menu")
    print("q : Quitter")
    print("=============================================\n")

    while True:
        choix = input("Insérez un choix : ")
        choix_str = str(choix).strip()

        if choix_str.upper() == "R":
            menu(conn)
            return
        elif choix_str.upper() == "Q":
            quit()

        try:
            choix_int = int(choix_str)
        except ValueError:
            print("Entrée invalide : veuillez entrer un numéro, R ou Q.")
            continue

        if choix_int == 1:
            update_frais_consultations(conn)           
        elif choix_int == 2:
            update_service_personnel(conn)
        else:
            print("Numéro de choix inconnu...")




def select_tous_les_services(conn):
    """
    Affiche la liste de tous les services.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT * 
                FROM Services
                """)
    columns = [description[0] for description in cur.description]
    table = PrettyTable(columns)

    rows = cur.fetchall()

    for row in rows:
        table.add_row(row)
        
    print(table)
    
    
    
    
    

def select_tout_le_personnel(conn):
    """
    Affiche la liste de tout le personnel.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT * 
                FROM Personnel
                """)
    columns = [description[0] for description in cur.description]
    table = PrettyTable(columns)

    rows = cur.fetchall()

    for row in rows:
        table.add_row(row)
        
    print(table)
    
    


def select_tous_les_patients(conn):
    """
    Affiche la liste de tous les patients depuis la vue Patients.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT * 
                FROM Patients
                """)
    columns = [description[0] for description in cur.description]
    table = PrettyTable(columns)

    rows = cur.fetchall()

    for row in rows:
        table.add_row(row)
        
    print(table)



def select_toutes_les_maladies(conn):
    """
    Affiche la liste de toutes les maladies depuis la vue Maladies.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT * 
                FROM Maladies
                """)
    columns = [description[0] for description in cur.description]
    table = PrettyTable(columns)

    rows = cur.fetchall()

    for row in rows:
        table.add_row(row)
        
    print(table)




def select_toutes_les_consultations(conn):
    """
    Affiche la liste de toutes les consultations.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT * 
                FROM Consultations
                """)
    columns = [description[0] for description in cur.description]
    table = PrettyTable(columns)

    rows = cur.fetchall()

    for row in rows:
        table.add_row(row)
        
    print(table)



def select_personnel_patients(conn):
    """
    Affiche la liste de tous les couples Personnel-Patients.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT * 
                FROM PersonnelPatients
                """)
    columns = [description[0] for description in cur.description]
    table = PrettyTable(columns)

    rows = cur.fetchall()

    for row in rows:
        table.add_row(row)
        
    print(table)



def select_patient_service(conn):
    """
    Affiche la liste de tous les couples Patients-Services.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT * 
                FROM PatientsServices
                """)
    columns = [description[0] for description in cur.description]
    table = PrettyTable(columns)

    rows = cur.fetchall()

    for row in rows:
        table.add_row(row)
        
    print(table)



def select_patient_maladie(conn):
    """
    Affiche la liste de tous les couples Patients-Maladies avec leur gravité.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT * 
                FROM PatientsMaladies
                """)
    columns = [description[0] for description in cur.description]
    table = PrettyTable(columns)

    rows = cur.fetchall()

    for row in rows:
        table.add_row(row)
        
    print(table)
    
    


def select_service_maladie(conn):
    """
    Affiche la liste de tous les services avec les maladies qu'ils gèrent.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT * 
                FROM ServicesMaladies
                """)
    columns = [description[0] for description in cur.description]
    table = PrettyTable(columns)

    rows = cur.fetchall()

    for row in rows:
        table.add_row(row)
        
    print(table)




def select_patients_ayant_grippe(conn):
    """
    Affiche la liste de tous les patients ayant la grippe.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
SELECT numero_patient, nom_patient, prenom_patient
FROM PatientsMaladies JOIN Patients_base USING (numero_patient)
WHERE nom_maladie = 'Grippe';
                """)
    columns = [description[0] for description in cur.description]
    table = PrettyTable(columns)

    rows = cur.fetchall()

    for row in rows:
        table.add_row(row)
        
    print(table)




def select_patients_ayant_maladie(conn):
    """
    Affiche la liste de tous les patients ayant une certaine maladie.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()

    listeMaladie=[]
    listePatientMaladie=[]

    for (i,) in cur.execute("SELECT nom_maladie FROM Maladies_base"):
        listeMaladie.append(i)
    print("\n\n Liste des Maladies \n")
    table_maladies = PrettyTable(["nom_maladie"])
    for m in listeMaladie:
        table_maladies.add_row([m])
    print(table_maladies)


    for (i,) in cur.execute("SELECT nom_maladie FROM PatientsMaladies"):
        listePatientMaladie.append(i)


 
    flagMaladie = False
    while flagMaladie == False:
        maladie = input("\nEntrez la maladie que vous souhaitez : ")
        if maladie not in listeMaladie and maladie not in listePatientMaladie:
            print("Nom de maladie invalide\n")
        elif maladie in listeMaladie and maladie not in listePatientMaladie:
            print("Aucun patient n'a cette maladie\n")
            return
        else:
            flagMaladie = True 
            cur.execute(
                "SELECT numero_patient, nom_patient, prenom_patient "
                "FROM PatientsMaladies JOIN Patients_base USING (numero_patient) "
                "WHERE nom_maladie = ?;",
                (maladie,)
            )    
    columns = [description[0] for description in cur.description]
    table = PrettyTable(columns)

    rows = cur.fetchall()

    for row in rows:
        table.add_row(row)
        
    print(table)




def select_utilisation_services(conn):
    """
    Affiche le nombre de patients qui utilisent un certain service.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    listeServices=[]
    listePatientService=[]
    
    cur.execute("""
                SELECT * 
                FROM Services
                """)
    columns = [description[0] for description in cur.description]
    table = PrettyTable(columns)

    rows = cur.fetchall()

    for row in rows:
        table.add_row(row)
        
    print(table)


    for (i,) in cur.execute("SELECT nom_service FROM Services"):
        listeServices.append(i)

    for (i,) in cur.execute("SELECT nom_service FROM PatientsServices"):
        listePatientService.append(i)

    flagMaladie = False
    while flagMaladie == False:
        service = input("\nEntrez le nom du service : ")
        if service not in listeServices and service not in listePatientService:
            print("Nom de service invalide\n")
        elif service in listeServices and service not in listePatientService:
            print("Aucun patient n'utilise ce service\n")
            return
        else:
            flagMaladie = True 
            cur.execute(
                "SELECT nom_service, COUNT(numero_patient) "
                "FROM PatientsServices WHERE nom_service = ? GROUP BY nom_service;",
                (service,)
            )
    columns = [description[0] for description in cur.description]
    table = PrettyTable(columns)

    rows = cur.fetchall()

    for row in rows:
        table.add_row(row)
        
    print(table)






def select_tous_les_medecins(conn):
    """
    Affiche la liste de tous les médecins.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
SELECT numero_personnel, nom_personnel, prenom_personnel
FROM Personnel
WHERE fonction_personnel = 'Médecin';
                """)
    columns = [description[0] for description in cur.description]
    table = PrettyTable(columns)

    rows = cur.fetchall()

    for row in rows:
        table.add_row(row)
        
    print(table)




def select_patients_abonnes(conn):
    """
    Affiche la liste des patients qui sont venus plus d'une fois.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
SELECT numero_patient, nom_patient, prenom_patient, Nbconsultations
FROM Patients
WHERE Nbconsultations > 1;
                """)
    columns = [description[0] for description in cur.description]
    table = PrettyTable(columns)

    rows = cur.fetchall()

    for row in rows:
        table.add_row(row)
        
    print(table)




def select_personnel_nonConsultations(conn):
    """
    Affiche la liste du personnel qui n'a effectué aucune consultation.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
SELECT numero_personnel
FROM Personnel
EXCEPT
SELECT numero_personnel
FROM Consultations;
                """)
    columns = [description[0] for description in cur.description]
    table = PrettyTable(columns)

    rows = cur.fetchall()

    for row in rows:
        table.add_row(row)
        
    print(table)




def insert_service(conn):
    """
    Insertion d'un service.

    Ou vérifie qu'on n'insère pas un service qui existe déjà.

    Prend en paramètre une connexion à la DB.
    Ne renvoie rien.
    """
    print("\nOn insère un service.")
    listServices = []
    cur = conn.cursor()

    for (i,) in cur.execute("SELECT nom_service FROM Services;"):
        listServices.append(i)
    
    option = input("Vous pouvez utiliser \"Nouveau\" ou \"Retour\" : ")

    flagChoisi = False
        
    if option.upper() == "NOUVEAU":
        flagChoisi = True
            
    elif option.upper() == "RETOUR":
        MenuInserer(conn)

    while flagChoisi == True:
        nomService = input("Entrez un nom de service : ")

        if nomService in listServices:
            print("Ce service existe déjà\n")

        else:
            #Confirmation du choix
            print("\nVérifiez votre choix :")
            print("Insérer le service \"",nomService,"\"")

            if input("Confirmez-vous ce choix? Y/N : ").upper() == "Y":
                #Requête SQL ici
                cur.execute("INSERT INTO Services VALUES (?);", (nomService,))
                print("\n" + "\33[32m" + "Success!" + "\33[0m" + " Vous pouvez vérfier votre insertion avec le menu Afficher")
                menu(conn)
                return
            else:
                print("\n" + "\33[91m" + "Vous refusez de confirmer..." + "\33[0m" + "Retour au menu.")
                menu(conn)
                return






def insert_personnel(conn):
    """
    Menu d'insertion d'un employé du personnel.

    Demande toutes les informations necéssaires à propos d'un employé.
    Vérifie les informations ayant des contraintes pour éviter d'éxécuter une requête fausse.
    Ou vérifier qu'on n'insère pas un employé qui existe déjà.

    Prend en paramètre une connexion à la DB.
    Ne renvoie rien.
    """
    print("\nOn insère quelqu'un au personnel.")
    listPersonnel = []
    listServices = []
    cur = conn.cursor()

    for (i,) in cur.execute("SELECT numero_personnel FROM Personnel;"):
        listPersonnel.append(i)
        
    for (i,) in cur.execute("SELECT nom_service FROM Services;"):
        listServices.append(i)
    
    option = input("Vous pouvez utiliser \"Nouveau\" ou \"Retour\" : ")

    flagNouveau = False
        
    if option.upper() == "NOUVEAU":
        flagNouveau = True
            
    elif option.upper() == "RETOUR":
        MenuInserer(conn)

    while flagNouveau == True:
        try:
            numPersonnel = int(input("Entrez un numéro de personnel : "))
        except ValueError:
            print("Entrée invalide : veuillez entrer un numéro.")
            continue

        if numPersonnel in listPersonnel:
            print("Ce numéro existe déjà\n")
        elif numPersonnel < 0 :
            print("Ce numéro est négatif\n")
        else:
            nomPersonnel = input("Entrez un nom : ")
            prenomPersonnel = input("Entrez un prénom : ")
            fonctionPersonnel = input("Entrez une fonction : ")
            flagService = False
            while flagService == False :  
                nomService = input("Enfin, entrez le nom du service dans lequel il travaille : ")                
                if nomService not in listServices:
                    print("Ce service n'existe pas")
                else:
                    flagService = True

                    #Confirmation du choix
                    print("\nVérifiez votre choix :")
                    print("Insérer l'employé de numéro \'", numPersonnel, "\' de nom \'", nomPersonnel, "\' de prénom \'", prenomPersonnel,
                         "\' de fonction \'", fonctionPersonnel, "\' travaillant dans le service \'", nomService, "\'")
        
                    if input("Vous confirmez ce choix? Y/N : ").upper() == "Y":
                        #Requête SQL ici
                        cur.execute(
                            "INSERT INTO Personnel VALUES (?, ?, ?, ?, ?);",
                            (numPersonnel, nomPersonnel, prenomPersonnel, fonctionPersonnel, nomService)
                        )
                        print("\n" + "\33[32m" + "Success!" + "\33[0m" +
                              " Vous pouvez vérfier votre insertion avec le menu Afficher")
                        menu(conn)
                        return
        
                    else:
                        print("\n" + "\33[91m" + "Vous refusez de confirmer..." + "\33[0m" + "Retour au menu.")
                        menu(conn)
                        return




def insert_patient(conn):
    """
    Menu d'insertion d'un patient.

    Demande toutes les informations necéssaires à propos d'un patient.
    Vérifie les informations ayant des contraintes d'éxécuter une requête fausse.

    Pour cela, utilise plusieurs requêtes SQL pour afficher les patients déjà existants.
    Ou vérifier qu'on n'insère pas un patient qui existe déjà.

    Prend en paramètre une connexion à la DB.
    Ne renvoie rien.
    """
    print("\nOn insère un patient.")
    listPatients = []
    cur = conn.cursor()

    for (i,) in cur.execute("SELECT numero_patient FROM Patients_base;"):
        listPatients.append(i)
         
    option = input("Vous pouvez utiliser \"Nouveau\" ou \"Retour\" : ")

    flagNouveau = False
        
    if option.upper() == "NOUVEAU":
        flagNouveau = True
            
    elif option.upper() == "RETOUR":
        MenuInserer(conn)

    while flagNouveau == True:
        try:
            numPatient = int(input("Entrez un numéro de patient : "))
        except ValueError:
            print("Entrée invalide : veuillez entrer un numéro.")
            continue

        if numPatient in listPatients:
            print("Ce numéro existe déjà\n")
            continue

        elif numPatient < 0 :
            print("Ce numéro est négatif\n")
            continue

        nomPatient = input("Entrez un nom : ")
        prenomPatient = input("Entrez un prénom : ")

        while True:
            print("Il nous faut maintenant la date de naissance.")
            while True:
                jour = input("Entrez un numéro de jour au format DD : ").strip()
                try:
                    jour_int = int(jour)
                except ValueError:
                    print("Entrée invalide : veuillez entrer un jour numérique.")
                    continue

                if not (1 <= jour_int <= 31):
                    print("Entrez un jour entre 1 et 31...")
                    continue

                else: #On a entré un jour entre 1 & 31
                    jour = f"{jour_int:02d}"
                    while True:
                        mois = input("Entrez un numéro de mois au format MM : ").strip()
                        try:
                            mois_int = int(mois)
                        except ValueError:
                            print("Entrée invalide : veuillez entrer un mois numérique.")
                            continue

                        if not (1 <= mois_int <= 12):
                            print("Entrez un mois entre 1 et 12...")
                            continue

                        else: #On a entré un mois entre 1 & 12
                            mois = f"{mois_int:02d}"
                            flagChoisi = False
                            while flagChoisi == False:
                                annee = input("Entrez une année au format YYYY : ").strip()
                                try:
                                    annee_int = int(annee)
                                except ValueError:
                                    print("Entrée invalide : veuillez entrer une année numérique.")
                                    continue

                                if annee_int < 0:
                                    print("L'année ne peut pas être négative")
                                elif annee_int > 9999:
                                    print("La base de données n'est pas faite pour prendre en compte les années à 5 chiffres...")
                                else:
                                    annee = f"{annee_int:04d}"
                                    flagChoisi = True

                                    #On formate la date au format DD-MM-YYYY
                                    date = jour + '-' + mois + '-' + annee
            
            
                                    adressePatient = input("Entrez une adresse (ville) : ")

                                    #Confirmation du choix
                                    print("\nVérifiez votre choix :")
                                    print("Insérer le patient de numéro \'", numPatient, "\' de nom \'", nomPatient, "\' de prénom \'", prenomPatient,
                                          "\' de date de naissance \'", date, "\' d'adresse \'", adressePatient, "\'")
        
                                    if input("Vous confirmez ce choix? Y/N : ").upper() == "Y":
                                        cur.execute(
                                            "INSERT INTO Patients_base VALUES (?, ?, ?, ?, ?);",
                                            (numPatient, nomPatient, prenomPatient, date, adressePatient)
                                        )
                                        print("\n" + "\33[32m" + "Success!" + "\33[0m" +
                                              " Vous pouvez vérfier votre insertion avec le menu Afficher")
                                        menu(conn)
                                        return
        
                                    else:
                                        print("\n" + "\33[91m" + "Vous refusez de confirmer..." + "\33[0m" + "Retour au menu.")
                                        menu(conn)
                                        return



def insert_personnelpatient(conn):
    """
    Insère un couple personnel-patient.

    Demande les numéros du personnel et du patient.
    Vérifie les informations ayant des contraintes pour éviter d'éxécuter une requête fausse.

    Pour cela, utilise plusieurs requêtes SQL pour afficher les personnes déjà existants.
    Ou vérifier qu'on n'insère pas un duo qui existe déjà.

    Prend en paramètre une connexion à la DB.
    Ne renvoie rien.
    """
    print("\nOn insère un couple personnel-patient.\n")
    
    listPersonnel = []
    listPatients = []
    cur = conn.cursor()

    for (i,) in cur.execute("SELECT numero_personnel FROM Personnel;"):
        listPersonnel.append(i)
        
    for (k,) in cur.execute("SELECT numero_patient FROM Patients_base;"):
        listPatients.append(k)   
            
    option = input("Vous pouvez utiliser \"Nouveau\" ou \"Retour\" : ")

    flagNouveau = False
        
    if option.upper() == "NOUVEAU":
        flagNouveau = True
            
    elif option.upper() == "RETOUR":
        MenuInserer(conn)

    while flagNouveau == True:
        try:
            numPersonnel = int(input("Commencez par choisir un numéro de de personnel : "))
        except ValueError:
            print("Entrée invalide : veuillez entrer un numéro.")
            continue

        if numPersonnel not in listPersonnel:
            print("Ce numéro de personnel n'existe pas\n")
        elif numPersonnel < 0 :
            print("Ce numéro est négatif\n")
        else:
            listPersonnelPatients = []
            cur = conn.cursor()
            for (i, j) in cur.execute("SELECT numero_personnel, numero_patient FROM PersonnelPatients"): #Requête SQL ici
                listPersonnelPatients.append((i, j))
            while True:
                flagPatient = False
                while flagPatient == False :
                    try:
                        numPatient = int(input("Entrez un numéro de patient : "))
                    except ValueError:
                        print("Entrée invalide : veuillez entrer un numéro.")
                        continue
                    if numPatient not in listPatients:
                        print("\nCe numéro de patient n'existe pas\n")
                    elif numPatient < 0 :
                        print("Ce numéro est négatif")
                    else:
                        flagPatient = True
                if (numPersonnel, numPatient) in listPersonnelPatients:
                    print("Cet employé s'occupe déjà de ce patient\n")
                else:
                    #Confirmation du choix
                    print("\nVérifiez votre choix :")
                    print("Insérer l'employé de numéro \'", numPersonnel, "\' avec le patient de numéro \'", numPatient, "\'")
        
                    if input("Vous confirmez ce choix? Y/N : ").upper() == "Y":
                        #Requête SQL ici
                        cur.execute("INSERT INTO PersonnelPatients VALUES (?, ?);", (numPersonnel, numPatient))
                        print("\n" + "\33[32m" + "Success!" + "\33[0m" +
                              " Vous pouvez vérfier votre insertion avec le menu Afficher")
                        menu(conn)
                        return
        
                    else:
                        print("\n" + "\33[91m" + "Vous refusez de confirmer..." + "\33[0m" + "Retour au menu.")
                        menu(conn)
                        return




def delete_from_consultations(conn):
    """
    Supprime une consultation de la table Consultations.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
  
    listTableConsultations = []
    listCodeConsultations = []
    
    for (i, j, k, l, m, n, o) in cur.execute("SELECT * FROM Consultations"):
         listTableConsultations.append((i, j, k, l, m, n, o))
 
    for (i,) in cur.execute("SELECT code_consultation FROM Consultations"):
        listCodeConsultations.append(i)
 
    #Affichage de la table Consultations
    """print("\n\n_______________ Liste des Consultations _______________\n")
    print("Code consultation — Numéro patient — Numéro personnel — Type consultation — Nom service — Date de consultation — Frais de consultation\n")
    for idx in range(0, len(listTableConsultations)):
        print(str(listTableConsultations[idx][0]) + " — " + str(listTableConsultations[idx][1]) + " — "
               + str(listTableConsultations[idx][2]) + " — " + str(listTableConsultations[idx][3]) + " — " + str(listTableConsultations[idx][4]) + " — " + str(listTableConsultations[idx][5]) +  " — " + str(listTableConsultations[idx][6]))
    print("____________________________________________________")"""
    select_toutes_les_consultations(conn)
    print("\n\nChoisissez un code de consultation à supprimer (première colonne)")
    print("Ou utilisez \"Retour\".")
    while True:

        choix = input("\nEntrez un numéro (ou RETOUR) : ").strip()
    
        if str(choix).upper() == "RETOUR":
             menu(conn)
             return
        try:
            choix_int = int(choix)
        except ValueError:
            print("Entrée invalide...")
            continue

        if (choix_int <= 0 or choix_int not in listCodeConsultations):
             print("Numéro de choix invalide...")
        else: #On a entré un numéro valide
    
             #Confirmation du choix
             print("Confirmez votre choix : ")
             print("Supprimer la consultation de code \"", choix_int , "\"", sep="")
             if input("\nConfirmez-vous ce choix ? Y/N : ").upper() == "Y":
                 cur.execute("DELETE FROM Consultations WHERE code_consultation =" + str(choix_int) + ";")#Requête SQL ici
                 print("\n" + "\33[32m" + "Success!" + "\33[0m" +
                       " Vous pouvez vérfier votre insertion avec le menu Afficher")
                 menu(conn)
                 return
    
             else:
                 print(
                     "\n" + "\33[91m" + "Vous refusez de confirmer..." + "\33[0m" + "Retour au menu.")
                 menu(conn)
                 return
    




def delete_from_services(conn):
    """
    Supprime un service de la table Services sans supprimer le personnel ni l'historique.
    Réaffecte les références vers un service par défaut ("Non affecté") puis supprime le service.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()

    # Récupérer la liste des services existants
    listServices = [row[0] for row in cur.execute("SELECT nom_service FROM Services")]

    # Affichage
    print("\n\n_______________ Liste des Services _______________\n")
    for s in listServices:
        print(s)
    print("___________________________________________________")

    while True:
        choix = input("\nEntrez un nom de service à supprimer (ou RETOUR) : ").strip()

        if choix.upper() == "RETOUR":
            menu(conn)
            return

        if choix not in listServices:
            print("Nom de service invalide...")
            continue

        if choix == "Non affecté":
            print("Vous ne pouvez pas supprimer le service 'Non affecté'.")
            continue

        # Confirmation
        print("\nConfirmez votre choix :")
        print("Supprimer le service \"", choix, "\" (le personnel et les consultations seront réaffectés à 'Non affecté')", sep="")
        if input("\nConfirmez-vous ce choix ? Y/N : ").upper() != "Y":
            print("\n" + "\33[91m" + "Vous refusez de confirmer..." + "\33[0m" + " Retour au menu.")
            menu(conn)
            return

        try:
            # 1) Créer le service par défaut s'il n'existe pas
            cur.execute("SELECT 1 FROM Services WHERE nom_service = ?;", ("Non affecté",))
            if cur.fetchone() is None:
                cur.execute("INSERT INTO Services(nom_service) VALUES (?);", ("Non affecté",))

            # 2) Réaffecter le personnel vers "Non affecté"
            cur.execute(
                "UPDATE Personnel SET nom_service = ? WHERE nom_service = ?;",
                ("Non affecté", choix)
            )

            # 3) Réaffecter les consultations vers "Non affecté"
            # (Même si votre schéma n'a pas explicitement une FK sur Consultations.nom_service,
            #  c'est cohérent et évite de garder des noms de services supprimés.)
            cur.execute(
                "UPDATE Consultations SET nom_service = ? WHERE nom_service = ?;",
                ("Non affecté", choix)
            )

            # 4) Supprimer les dépendances directes au service
            cur.execute("DELETE FROM PatientsServices WHERE nom_service = ?;", (choix,))
            cur.execute("DELETE FROM ServicesMaladies WHERE nom_service = ?;", (choix,))

            # 5) Supprimer le service
            cur.execute("DELETE FROM Services WHERE nom_service = ?;", (choix,))

            conn.commit()

            print("\n" + "\33[32m" + "Success!" + "\33[0m" +
                  " Service supprimé. Le personnel et les consultations ont été réaffectés à 'Non affecté'.")
            menu(conn)
            return

        except sqlite3.Error as e:
            conn.rollback()
            print("\n\33[91mErreur SQLite:\33[0m", e)
            menu(conn)
            return





def drop_all_tables(conn):
    """
    Supprime toutes les tables et vues. 
    Ceci était pour un essai, ce n'était pas demandé.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    
    print("Attention ! Vous êtes sur le point de supprimer toutes les tables et vues !")
    reponse = input("Etes-vous sûrs de votre choix ? y/n : ")
    
    if str(reponse).upper() == "Y" :        
        cur.execute("DROP VIEW IF EXISTS Maladies;")
        cur.execute("DROP VIEW IF EXISTS Patients;")
        cur.execute("DROP TABLE IF EXISTS Consultations;")
        cur.execute("DROP TABLE IF EXISTS ServicesMaladies;")
        cur.execute("DROP TABLE IF EXISTS PatientsMaladies;")
        cur.execute("DROP TABLE IF EXISTS Maladies_base;")
        cur.execute("DROP TABLE IF EXISTS PatientsServices;")
        cur.execute("DROP TABLE IF EXISTS PersonnelPatients;")
        cur.execute("DROP TABLE IF EXISTS Patients_base;")
        cur.execute("DROP TABLE IF EXISTS Personnel;")
        cur.execute("DROP TABLE IF EXISTS Services;")
    else :
        menu(conn)
        return




def update_frais_consultations(conn):
    """
    Augmente les frais de consultations de 20%.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("UPDATE Consultations SET frais_consultation = frais_consultation * 1.2;")
    
    


def update_service_personnel(conn):
    """
    Modifie le service dans lequel travaille un membre du personnel.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT * 
                FROM Personnel
                """)
    columns = [description[0] for description in cur.description]
    table = PrettyTable(columns)

    rows = cur.fetchall()

    for row in rows:
        table.add_row(row)
        
    print(table)

    listPersonnel = []    
    for (i,) in cur.execute("SELECT numero_personnel FROM Personnel"):
         listPersonnel.append(i)
         
    listServices = []    
    for (i,) in cur.execute("SELECT nom_service FROM Services"):
         listServices.append(i)

    flagPersonnel = False

    while flagPersonnel == False:    
        try:
            numPersonnel = int(input("\nEntrez le numéro du personnel dont vous voulez changer le service : "))
        except ValueError:
            print("ERREUR : Numéro de personnel invalide")
            continue
        if numPersonnel not in listPersonnel or numPersonnel < 0 :
            print("ERREUR : Numéro de personnel invalide")
        else :
            flagService = False
            while flagService == False:
                service = input("\nEntrez le nom du nouveau service dans lequel il travaille : ")
                if service not in listServices:
                    print("ERREUR : Nom de service invalide")
                else:
                    print("\nConfirmez votre choix :")
                    print("Le personnel de numéro", numPersonnel, "travaillera désormais dans le service '",service, "'")
                    if input("\nConfirmez-vous ce choix ? Y/N : ").upper() == "Y":
                        cur.execute("UPDATE Personnel SET nom_service = ? WHERE numero_personnel = ?;", (service, numPersonnel))
                        print("\n" + "\33[32m" + "Success!" + "\33[0m" +
                              " Vous pouvez vérfier votre insertion avec le menu Afficher")
                        menu(conn)
                        return   
                    else:
                        print("\n" + "\33[91m" + "Vous refusez de confirmer..." + "\33[0m" + "Retour au menu.")
                        menu(conn)
                        return




def main():
    # Nom de la BD à créer
    db_file = "data/Projet.db"

    # Créer une connexion a la BD
    try:
        db.initialiser_bd(db_file)
    except Exception as e:
        print("Erreur lors de l'initialisation de la base :", e)
        quit()    

    conn = db.creer_connexion(db_file)
    if conn is None:
        print("Impossible d'ouvrir la base de données.")
        quit()

    # Remplir la BD
    #print("On crée la bd et on l'initialise avec des premières valeurs.")
    #db.mise_a_jour_bd(conn, "data/Projet.sql")
    #db.mise_a_jour_bd(conn, "data/Insert_OK.sql")

    print("\n\nBienvenue dans la base de données du hameau de santé.\n")
    menu(conn)
    return


if __name__ == "__main__":
    main()
