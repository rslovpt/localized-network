class db_handler:
    def __init__(self):
        pass

    def createDataBase(self, ID : str, AUTH_ID ,dataSet=None) -> str:
        reciept = None
        try:
            with open("storage_/"+str(ID), "x+") as db_file:
                db_file.write(str(AUTH_ID))
                if dataSet != None:
                    formated = ""
                    for i in dataSet:
                        formated += "\n"+str(i)
                    db_file.write(formated); reciept = "FILE_CREATED_WITH_DATA"
                else:
                    reciept = "FILE_CREATED_WITHOUT_DATA"        
        except FileExistsError:
            reciept = "FILE_EXIST"
        
        return reciept
    
    def accessDataBase(self, AUTH_ID):
        pass