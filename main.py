import RegistrationManagement as rm
import csv

def main():
    #Fill your code for getting user inputs, objects creation,invoking functions 
    #and display statements
    reg = rm.RegistrationManagement()
    file = input("Enter the file name\n")
    f = open(file , "r")
    lines = f.readlines()
    for line in lines:
        arr = line.split(",")
        if(reg.validate_registration_number(arr[1])):
            reg.add_bill_details(arr[0] , arr[1] , arr[2] , arr[3])
    f.close()
    print("Number of valid records is",len(reg.bill_list))
    reg_no = input("Enter the Registration Number\n")
    billd =reg.view_bill_by_registration_number(reg_no)
    if(billd == None):
        print("No records found");
    else:
        print("Bill Number {0}\nCustomer Name {1}\nPhone Number {2}".format(billd.get_bill_number() , billd.get_consumer_name() , billd.get_mobile_number()));








if __name__=='__main__':
    main()
