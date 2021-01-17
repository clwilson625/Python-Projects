
#Parent Class User
class User:
      fname = "Joseph"
      lname = "Meeks"
      email = "josephm@gmail.com"
      password = "1234"

      def getLoginInfo(self):
            entry_fname = input("Enter your first name: ")
            entry_password = input("Enter your password: ")
            if (entry_fname == self.fname and entry_password == self.password):
                  print("Welcome back, {}".format(entry_fname))
            else:
                  print("The password or email is incorrect. ")

#Child Class Student1 - this is the first of 2 attributes for the student
class Student1(User):
      course_name = "Biology"
      student_ID = "9876"

#This will have the same method as the parent class ("User"), the difference
#is that instead of using entry_password, it will ask for entry_studentID and will display the students current class.

      def getLoginInfo(self):
            entry_lname = input("Enter your last name: ")
            entry_email = input("Enter your email: ")
            entry_student_ID = input("Enter your studentID: ")
            entry_course_name = input("Enter course name: ")
            if (entry_email == self.email):
                  print("Welcome to your student activity page {} !".format(entry_email))
            else:
                  print("The email or studenID you entered is not correct")

#Child Class Student2 - this is the 2nd attribute for the student
class Student2(User):
      currentGPA = "3.88"
      courses_left = "6"
#This will use the same method as the parent class ("User"), the difference is,
#it will ask for password and studentID to display the current GPA and courses left.
      def getLoginInfo(self):
            entry_password = input("Enter your password: ")
            if (entry_password == self.password):
                   print(" {}, your current GPA is, {}! ".format(entry_name, entry_currentGPA))
            else:
                  print("The password, or student ID is incorrect")

#The following code invokes the methods inside each class for User and Student

student = User()
student.getLoginInfo()

admin = Student1()
admin.getLoginInfo()

student2 = Student2()
student2.getLoginInfo()

            

      
