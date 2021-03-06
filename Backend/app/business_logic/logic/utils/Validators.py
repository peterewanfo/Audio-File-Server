
class ValidatorsClass():
    
    @staticmethod
    def validate_participants(participants):
        try:

            participants_length = len(participants)

            if participants_length <= 10:
                #LOOP TO ENSURE PARTICIPANTS NOT LARGER THAN 100 CHARACTERS

                for participant in participants:
                    if len(participant) > 100:
                        return False
                return True
            else:
                return False
        except Exception:
            return False