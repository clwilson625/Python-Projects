Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from abc import ABC, abstractmethod
>>> class car(ABC):
	#this is the parent class
	def creditAmount(self, amount):
		print("Your credit card purchase amount: ",amount)
	#this is passing an argument but does not tell us how or what
	#kind of data it will be

		
>>> @abstractmethod
	def payment(self, amount):
		
SyntaxError: unexpected indent
>>> def payment(self, amount):
	pass

>>> class CreditCardPurchase(car):
	#this is where I defined hot to implement the payment function from
	#the parent creditAmount class.

	def payment(self, amount):
		print('Your purchase amount of {} lowered your available balance to $12. '.format(amount))

		
>>> obj = CreditCardPurchase()
>>> obj.creditAmount("$327")
Your credit card purchase amount:  $327
>>> obj.payment("$327")
Your purchase amount of $327 lowered your available balance to $12. 
>>> 