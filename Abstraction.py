#  Abstraction

   
from abc import ABC, abstractmethod
class car (ABC):
      def payCheck(self, amount):
            print ("Your check amount is: ",amount)
# this function tells us to pass in an argument, but does not tell us how or what kind of data it will be
      @abstractmethod
      def payment(self, amount):
            pass

class witholding (car) :

# this is where we have defined the payment function from its parent paySlip class

      def payment(self, amount):
            print('Your check will be deducted {} for witholding purposes '.format(amount))

obj = witholding ()
obj.payCheck("$550")
obj.payment("$37.50")


