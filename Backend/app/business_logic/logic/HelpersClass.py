import traceback
import time
import datetime

class HelpersClass():
    
    @staticmethod
    def getDateFromTimeStamp(timestamp):
        
        converted = str(time.strftime("%A, %d %b %Y", time.localtime(int(timestamp) ) ) )

        return converted

    @staticmethod
    def getDateTimeFromTimeStamp(timestamp):
        
        conveted = str(time.strftime("%A, %d %b %Y, %I:%M%p", time.localtime(int(timestamp) ) ) )

        return converted