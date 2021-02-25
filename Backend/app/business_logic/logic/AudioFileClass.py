import traceback
import time
import datetime

from app.business_logic.utils.DBFunctionsClass import DBFunctionsClass
from app.business_logic.logic.HelpersClass import HelpersClass
from app.business_logic.utils.enum_audiofile import AudioFileEnum

class AudioFileClass():

    @staticmethod
    def createAudioFile(file_type, file_metadata):
        """CREATE AUDIO FILE"""

        try:

            #CHECK IF FILE TYPE IS ALLOWED
            is_allowed = str(file_type).upper() in [str(f_type.name).upper() for f_type in AudioFileEnum]

            if is_allowed:

                uploaded_time = int(time.time() )

                query = ""

                #GENERATE DATABASE INSERTION QUERY BASED ON FILE TYPE
                if AudioFileEnum[str(file_type).lower()].value == 1:

                    #{GENERATE QUERY STRING} INSERT TO SONG TABLE

                    query = f"""INSERT INTO Song(
                    song_name, song_duration, uploaded_time)
                    VALUES(
                    '{file_metadata["name"]}', '{file_metadata["duration"]}', '{uploaded_time}')"""

                elif AudioFileEnum[str(file_type).lower()].value == 2:

                    #{GENERATE QUERY STRING} INSERT TO PODCAST TABLE
                    query = f"""INSERT INTO Podcast(
                    name, duration, uploaded_time, host, participants)
                    VALUES(
                    '{file_metadata["name"]}', '{file_metadata["duration"]}', '{uploaded_time}', '{file_metadata["host"]}', '{file_metadata["participants"]}')"""

                elif AudioFileEnum[str(file_type).lower()].value == 3:

                    #{GENERATE QUERY STRING} INSERT TO AUDIOBOOK TABLE
                    query = f"""INSERT INTO Audiobook(
                    title, author, naration, duration, uploaded_time)
                    VALUES(
                    '{file_metadata["title"]}', '{file_metadata["author"]}', '{file_metadata["naration"]}', '{file_metadata["duration"]}', '{uploaded_time}')"""

                DBFunctionsClass.execCommitDb(query)

                return True

            else:
                return False

        except Exception:
            print(str(traceback.format_exc() ))
            return False

    @staticmethod
    def deleteAudioFile(file_type, id):
        """DELETE AUDIO FILE"""

        try:

            #CHECK IF FILE TYPE IS ALLOWED
            is_allowed = str(file_type).upper() in [str(f_type.name).upper() for f_type in AudioFileEnum]

            if is_allowed:

                uploaded_time = int(time.time() )

                query = ""

                #GENERATE DATABASE INSERTION QUERY BASED ON FILE TYPE
                if AudioFileEnum[str(file_type).lower()].value == 1:

                    #{GENERATE QUERY STRING} DELETE FROM SONG TABLE

                    query = f"""DELETE FROM Song WHERE id = '{id}'"""

                elif AudioFileEnum[str(file_type).lower()].value == 2:

                    #{GENERATE QUERY STRING} INSERT TO PODCAST TABLE
                    query = f"""DELETE FROM Podcast WHERE id = '{id}'"""

                elif AudioFileEnum[str(file_type).lower()].value == 3:

                    #{GENERATE QUERY STRING} INSERT TO AUDIOBOOK TABLE
                    query = f"""DELETE FROM Audiobook WHERE id = '{id}'"""

                DBFunctionsClass.execCommitDb(query)

                return True

            else:
                return False

        except Exception:
            print(str(traceback.format_exc() ))
            return False

    @staticmethod
    def updateAudioFile(file_type, file_metadata, id):
        """UPDATE AUDIO FILE"""

        try:

            #CHECK IF FILE TYPE IS ALLOWED
            is_allowed = str(file_type).upper() in [str(f_type.name).upper() for f_type in AudioFileEnum]

            if is_allowed:

                uploaded_time = int(time.time() )

                query = ""

                #GENERATE DATABASE INSERTION QUERY BASED ON FILE TYPE
                if AudioFileEnum[str(file_type).lower()].value == 1:

                    #{GENERATE QUERY STRING} UPDATE SONG TABLE

                    query = f"""UPDATE Song SET song_name = '{file_metadata["name"]}', song_duration = '{file_metadata["duration"]}' WHERE id = '{id}' """

                elif AudioFileEnum[str(file_type).lower()].value == 2:

                    #{GENERATE QUERY STRING} UPDATE PODCAST TABLE
                    query = f"""UPDATE Podcast SET name = '{file_metadata["name"]}', duration = '{file_metadata["duration"]}', host = '{file_metadata["host"]}', participants = '{file_metadata["participants"]}' WHERE id = '{id}' """

                elif AudioFileEnum[str(file_type).lower()].value == 3:

                    #{GENERATE QUERY STRING} INSERT TO AUDIOBOOK TABLE
                    query = f"""UPDATE Audiobook SET title = '{file_metadata["title"]}', author = '{file_metadata["author"]}', naration = '{file_metadata["naration"]}', duration = '{file_metadata["duration"]}'"""

                DBFunctionsClass.execCommitDb(query)

                return True

            else:
                return False

        except Exception:
            print(str(traceback.format_exc() ))
            return False

    
    @staticmethod
    def getAudioFile(file_type, file_id = False):
        """GET AUDIO FILE(S)"""

        try:

            #CHECK IF FILE TYPE IS ALLOWED
            is_allowed = str(file_type).upper() in [str(f_type.name).upper() for f_type in AudioFileEnum]

            if is_allowed:

                query = ""

                #1. CHECK FILE TYPE SELECTED
                if AudioFileEnum[str(file_type).lower()].value == 1:

                    #2. BUILD QUERY STRING IF QUERY IS FOR PARTICULAR FILE ID
                    
                    if file_id:
                        query = f"""SELECT * FROM Song WHERE id = '{file_id}'"""
                    else:
                        query = f"""SELECT * FROM Song"""

                elif AudioFileEnum[str(file_type).lower()].value == 2:

                    #2. BUILD QUERY STRING IF QUERY IS FOR PARTICULAR FILE ID
                    if file_id:
                        query = f"""SELECT * FROM Podcast WHERE id = '{file_id}' """
                    else:
                        query = f"""SELECT * FROM Podcast"""

                elif AudioFileEnum[str(file_type).lower()].value == 3:

                    #2. BUILD QUERY STRING IF QUERY IS FOR PARTICULAR FILE ID
                    if file_id:
                        query = f"""SELECT * FROM Audiobook WHERE id = '{file_id}'"""
                    else:
                        query = f"""SELECT * FROM Audiobook"""

                result = False
                if file_id:
                    result = DBFunctionsClass.execFetchOne(query)

                    if result:
                        result["uploaded_time"] = HelpersClass.getDateFromTimeStamp(result["uploaded_time"])
                else:
                    result = DBFunctionsClass.execFetchAll(query)
                    if result:
                        for d in result:
                            d["uploaded_time"] = HelpersClass.getDateFromTimeStamp(d["uploaded_time"])

                return result

            else:
                return False

        except Exception:
            print(str(traceback.format_exc() ))
            return False