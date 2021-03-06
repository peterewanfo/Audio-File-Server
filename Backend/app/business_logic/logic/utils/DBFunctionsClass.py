import mysql.connector as MySQLdb
import gc

class DBFunctionsClass():
    
    db = None
    cursor = None

    @staticmethod
    def connection():
        """
        Create new database connection
        returns database connection
        """

        from app.business_logic.db_models import DBModels

        database_name = DBModels.database_name
        database_password = DBModels.database_password

        db = MySQLdb.connect(host='localhost', user='root', password=database_password, database=database_name)

        # gc.collect()

        return db

    @classmethod
    def _closeDb(cls):
        """
        Close database Connection
        Ideal to use after page request
        """

        #CHECK IF DB IS NOT FALSE
        if cls.db:
            
            #ENSURE DB IS STILL CONNECTED
            if cls.db.is_connected():
                cls.cursor.close()
                cls.db.close()
                
                gc.collect()
            else:
                gc.collect()
        else:
            gc.collect()

    @classmethod
    def execFetchOne(cls, query):

        db = cls.connection()

        db_cursor = db.cursor(buffered=True, dictionary=True)
        db_cursor.execute(query)

        data = db_cursor.fetchone()

        # cls._closeDb()

        return data

    @classmethod
    def execFetchAll(cls, query):

        db = cls.connection()

        db_cursor = db.cursor(buffered=True, dictionary=True)
        db_cursor.execute(query)
        
        data = db_cursor.fetchall()

        # cls._closeDb()

        return data

    @classmethod
    def execCommitDb(cls, query):

        db = cls.connection()

        db_cursor = db.cursor(buffered=True, dictionary=True)
        db_cursor.execute(query)
        
        """
        Ensure Create,Update,Delete(CUD) operations are perform
        """
        db.commit()

        return True

        # cls._closeDb()

    @classmethod
    def manageDBConnection(cls):

        #CLOSE DATABASE
        cls._closeDb()

