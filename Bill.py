class Bill:
    def __init__(self):
        self.__bill_number=0
        self.__registration_number=""
        self.__consumer_name=""
        self.__mobile_number=0
    
    def get_bill_number(self):
        return self.__bill_number
    
    def set_bill_number(self,bill_number):
        self.__bill_number = bill_number
    
    def get_consumer_name(self):
        return self.__consumer_name
    
    def set_consumer_name(self,consumer_name):
        self.__consumer_name = consumer_name
    
    def get_registration_number(self):
        return self.__registration_number
    
    def set_registration_number(self,registration_number):
        self.__registration_number = registration_number
    
    def get_mobile_number(self):
        return self.__mobile_number
    
    def set_mobile_number(self,mobile_number):
        self.__mobile_number = mobile_number
