import os
import sqlite3

def initialiser_bd(db_path: str,
                   schema_sql: str = "data/Projet.sql",
                   data_sql: str = "data/Insert_OK.sql"):
    """
    Create and initialize the database if it does not exist.
    """
    if os.path.exists(db_path):
        return  # DB already exists, do nothing

    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    print("Initialisation de la base de données...")

    conn = sqlite3.connect(db_path)
    try:
        conn.execute("PRAGMA foreign_keys = ON")

        with open(schema_sql, encoding="utf-8") as f:
            conn.executescript(f.read())

        with open(data_sql, encoding="utf-8") as f:
            conn.executescript(f.read())

        conn.commit()
        print("Base de données initialisée.")
    finally:
        conn.close()


def creer_connexion(db_file):
    """Crée une connexion a la base de données SQLite spécifiée par db_file

    :param db_file: Chemin d'accès au fichier SQLite
    :return: Objet connexion ou None
    """

    try:
        conn = sqlite3.connect(db_file)
        # On active les foreign keys
        conn.execute("PRAGMA foreign_keys = ON")
        return conn
    except sqlite3.Error as e:
        print(f"Erreur SQLite : {e}")

    return None


def mise_a_jour_bd(conn: sqlite3.Connection, file: str):
    """Exécute sur la base de données toutes les commandes contenues dans le
    fichier fourni en argument.

    :param conn: Connexion à la base de données
    :type conn: sqlite3.Connection
    :param file: Chemin d'accès au fichier contenant les requêtes
    :type file: str
    """

    # Lecture du fichier et placement des requêtes dans un tableau
    try:
        with open(file, "r", encoding="utf-8") as f:
            sql_script = f.read()

        conn.executescript(sql_script)
        conn.commit()
    except (OSError, sqlite3.Error) as e:
        conn.rollback()
        raise RuntimeError(f"Failed to execute SQL script '{file}': {e}") from e
