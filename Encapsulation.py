#Encapsulation  Page 236


#  This is an encapsulation using the Private attribute
#  Private uses two __ underscores to denote it

class Protected:
      def __init__(self):
            self.__privateVar = 47

      def getPrivate(self):
            print(self.__privateVar)

      def setPrivate(self, private):
            self.__privateVar = private

obj = Protected()
obj.getPrivate()
obj.setPrivate(19)
obj.getPrivate()

#  This is an encapsulation using the Protected attribute
#  Protected uses one _ underscore to denote it  


class Protected:
      def __init__(self):
            self._protectedVar = 0

obj = Protected()
obj._protectedVar = 26
print(obj._protectedVar)
