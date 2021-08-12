import Bill as bl


class RegistrationManagement:
    def __init__(self):
        self.bill_list=[]
    
    
    def add_bill_details(self,bill_no,reg_no,con_name,mob_no):
        # REMOVE THE BELOW KEY WORD 'pass' and fill  your code here 
        bill_obj = bl.Bill()
        bill_obj.set_bill_number(bill_no)
        bill_obj.set_registration_number(reg_no)
        bill_obj.set_consumer_name(con_name)
        bill_obj.set_mobile_number(mob_no)
        self.bill_list.append(bill_obj)
        
    
    
    def view_bill_by_registration_number(self,reg_no):
        # REMOVE THE BELOW KEY WORD 'pass' and fill your code here 
        for i in self.bill_list:
            if(i.get_registration_number() == reg_no):
                return i
        return None
        
       
        
    
    def validate_registration_number(self,reg_no):
        # REMOVE THE BELOW KEY WORD 'pass' and fill your code here 
        s1 = reg_no[0:4]
        s2 = reg_no[len(reg_no)-2 : len(reg_no)]
        if(s1 == "KL52" and s2.isdigit() and len(reg_no) == 10):
            return True
        else:
            print("Invalid Registration Number\n")
            return "Invalid Registration Number"
