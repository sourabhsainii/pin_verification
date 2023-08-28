from model.pin import Pin
from model.group import Group
from model.pin_verify_request import PinVerifyRequest
from sqlalchemy import exc
from sqlalchemy.orm.exc import NoResultFound


from dbConfig.dbConfig import intializeDB

class verifyPinService():

    def   __init__(self):
            self.dbSession =  intializeDB.createDBSession()
    
    def verifyPin(
            self,
            request:PinVerifyRequest
    ):
        try:
                print("request::::::: ", request["applicationId"])
                group_id = request['applicationId']
                pin = request['pin']
 
                if len(pin) < 10:
                    print("Invalid Pin")
                    return 
                
                
                self.dbSession.query(Group).get(group_id)
                
                self.dbSession.query(Pin).filter_by(pin=pin,group_id=group_id).one()
                
                print("valid pin")
                return 'valid pin'
        
        except NoResultFound:
            print("Invalid pin or group not found")
            return "Invalid pin or group not found"

        except Exception as e:
                print('Error in verifyPin::',e)
                return e
        
        finally:
            self.dbSession.close()