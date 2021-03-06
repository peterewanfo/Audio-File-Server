import mysql.connector as MySQLdb
import time
import passlib
from passlib.hash import sha256_crypt

class DBModels():

    db = None
    cursor = None
    database_name = "AudioFileServerDB"
    database_password = "password"

    #NOTE -> PASSWORD AND DATA SHOULD BE SAVED ON ENVIRONMENT VARIABLES ON PRODUCTION

    can_init_db = False

    @classmethod
    def dbConnect(cls):
        cls.db = MySQLdb.connect(host='localhost', user='root', password=cls.database_password)

        cls.cursor = cls.db.cursor(buffered=True)

        try:
            cls.createTable(f'DROP DATABASE IF EXISTS {cls.database_name}')
            cls.cursor.execute(f'USE {cls.database_name}')

        except Exception:

            cls.createTable(f'DROP DATABASE IF EXISTS {cls.database_name}')

            cls.cursor.execute(f'CREATE DATABASE IF NOT EXISTS {cls.database_name}')

            cls.cursor.execute(f'USE {cls.database_name}')
            
            cls.can_init_db = True

    @classmethod
    def createTable(cls, query):

        cls.cursor.execute(query)
        
        cls.db.commit()

    @classmethod
    def initDatabase(cls):
            
        cls.dbConnect()

        ########################################################
        #--------DATABASE CREATE --------------------#
        ########################################################

        #TABLE TO HOLD SONG RECORDS
        cls.createTable("CREATE TABLE IF NOT EXISTS Song("
                    "id INT(11) PRIMARY KEY AUTO_INCREMENT, "
                    "song_name VARCHAR(100), "
                    "song_duration INT(11), "
                    "uploaded_time INT(11) "
                    ") ENGINE = InnoDB;")

        #TABLE TO HOLD PODCAST RECORDS
        cls.createTable("CREATE TABLE IF NOT EXISTS Podcast("
                    "id INT(11) PRIMARY KEY AUTO_INCREMENT, "
                    "name VARCHAR(100), "
                    "duration INT(11), "
                    "uploaded_time INT(11), "
                    "host VARCHAR(100), "
                    "participants LONGTEXT "
                    ") ENGINE = InnoDB;")

        #TABLE TO HOLD AUDIOBOOK RECORDS
        cls.createTable("CREATE TABLE IF NOT EXISTS Audiobook("
                    "id INT(11) PRIMARY KEY AUTO_INCREMENT, "
                    "title VARCHAR(100), "
                    "author VARCHAR(100), "
                    "narator VARCHAR(100), "
                    "duration INT(11), "
                    "uploaded_time INT(11) "
                    ") ENGINE = InnoDB;")
