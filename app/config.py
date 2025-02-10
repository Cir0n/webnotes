import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv()

# Configuration globale et gestion de la base de données
class Config:
    # Variables d'environnement pour la configuration
    DB_HOST = os.getenv('DB_HOST')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_NAME')
    SECRET_KEY = os.getenv('SECRET_KEY')


# Classe de gestion des connexions à la base de données
class Database:
    def __init__(self):
        # Initialisation de la connexion MySQL avec support UTF-8
        self.connection = mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME,
            charset='utf8mb4',
            collation='utf8mb4_unicode_ci'
            )
        self.cursor = self.connection.cursor(dictionary=True)

    def query(self, query, values=None):
        # Exécute une requête et retourne les résultats
        self.cursor.execute(query, values)
        return self.cursor.fetchall()

    def execute(self, query, values=None):
        # Exécute une requête sans retour de résultats
        self.cursor.execute(query, values)
        self.connection.commit()

    def close(self):
        # Ferme les connexions à la base de données
        self.cursor.close()
        self.connection.close()
