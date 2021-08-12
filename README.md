# Bike_Show_Room_Software
Bike Show Room
Guevara Motor Bike Showroom is one of the top showrooms for bikes. As the number of transactions are drastically increasing, they wish to automate the work process.  To start with they need to automate the process for the motor bike sold from their showroom.  As a programmer, help them to do this by developing a Python program.

Whenever a bike is sold, the showroom records the details in a file, named billDetails.txt. The details stored in the file are bill number, registration number, customer name, and mobile number. The application needs to retrieve the data from the file and process the data.

The file containing bill details is delimited using the comma (,).

[bill_number, registration_umber, customer_name, mobile_number]

2348, KL52AC1251, James,9568412301

2343,KL52A96547,Sam,9658742541


Component Specification: Bill (model class)  - Template is been given

Type(Class)

Attributes

Methods

Responsibilities

Bill

bill_number - integer type

registration_number - string type

consumer_name - string type

mobile_number - integer type

Include getters and setters method for all the attributes.




Component Specification: RegistrationManagement(Utility Class)

Type(Class)

Attributes

Methods

Responsibilities

RegistrationManagement


bill_list - List type




Note:  All the class attributes should be declared as private.

Requirement 1: Validate Registration number

The method validate_registration_number() accepts registration_number as input and returns True if it is valid. Else it should display and return the message "Invalid Registration Number".

Component Specification: RegistrationManagement(Utility Class)

Component Name

Type(Class)

Methods

Responsibilities
Validate the registration number according to the specifications given

RegistrationManagement

validate_registration_number( self, reg_no)

Validate the registration number, if valid return True else this method should return and display the specified message


The assumption for Valid Registration Number :

The length of the registration number must be 10, the first four letters are equal to “KL52”, and the last two digits are numbers.

Requirement 2: add_bill_details()

This method takes the bill details as ists parameters and createss a Bill object and sets the the value and then  adds that object into the bill details list.

Component Specification: RegistrationManagement(Utility Class)

Component Name

Type(Class)

Methods

Responsibilities

Create the Bill object and set the  values and add the Bill object to  the list 

RegistrationManagement

add_bill_details(self,bill_no,reg_no,con_name,mob_no)

This method should create the bill object and set the values that are passed as a parameter to the function and add the bill object to the bill_list


Requirement 3: View bill by registration number

This method view_bill_by_registration_number() takes the registration number as input and returns the bill object pertaining to that number.

Component Specification: RegistrationManagement (Utility Class)

Component Name

Type(Class)

Methods

Responsibilities

View the bill details for a particular registration

RegistrationManagement

view_bill_by_registration_number( reg_no)

This method should return the bill object based on the parameter passed.


In the main() method,

Get the name of the file as input (like billDetails.txt) from the user.

Retrieve the data from the file and parse the bill record details, invoke the validate_registration_number () method.

If the registration number is valid then invoke the add_bill_details() method by passing the bill details as to its parameters.

If the registration number is not valid then display the message “Invalid Registration Number”.

Continue to parse the next record until it reaches the last record.

Next invoke the view_bill_by_registration_number() method. This method takes the registration number as the argument. Based on the registration number, find the bill details and return that object else return None. 

If the view_bill_by_registration_number() method returns None, then display “No records found” in the main() method.

Display the bill details as shown in the sample Input / Output.

Note:

In the sample input/output provided, the highlighted text in bold corresponds to the input given by the user and the remaining text represents the output.

Ensure to follow the object-oriented specifications provided in the question description.
Ensure to provide the names for classes, attributes, and methods as specified in the question description.

Adhere to the code template, if provided.  Please do not change the code template given.

Assume billDetails.txt has the below contents





Sample Input / Output:

Enter the file name

billDetails.txt

Invalid Registration Number

Invalid Registration Number

Number of valid records is 6


Enter the Registration Number

KL52AF6943

Bill Number 2344

Customer Name Alex

Phone Number 6352487549

Core Programming
General
Unix Fundamentals and Scripting
File System
Filters
Vi Editor
Bourne Shell
Python programming - Course Introduction
Introduction to Python
Control Structures
Lists,Tuples and Dictionaries
Functions and Modules
Working with Files
Class and Objects
Challenge Yourself!
Python References
Help Desk
Dashboard
Performance Dashboard
Help Desk
FAQs
Discussion Community
Practice editor
      
Powered by Tekstac
