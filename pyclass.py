
def __init__(self, name, email, password, account):
      self.name = name
      self.email = email
      self.password = password
      self.account = account

      New_user = User("John Doe", "jdoe@outlook.com", "p@ssw0rd", 1234)

      #from Python course page 198


      class User:
            name = 'No Name Provided'
            email = ' '
            password = '1234abcd'
            account_number = 0

      class Employee(User):
            base_pay = 11.00
            department = 'General'

      class Customer(User):
            mailing_address = ' '
            mailing_list = True


      #my Inheritance Assignment

      #This is the area for the basic information for the user

      class User:
            name = 'No Name Provided'
            login = ' '
            password = 'a1b2c3d4'
            student_ID = 0

      ##child class for the User.  This area will provide a professors name and course 

      class Course(User):
            professor_name = 'Smith'
            course = Astronomy

      #child class for the User.  This area will provide a mailing address and will show that the student has alumni status

      class Student(User):
            mailing_address = ' '
            alumni = True

      
            
