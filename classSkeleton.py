class myObj(object):
	def __init__(self):
		print "i have been intiated...."
		
	def func1(self):
		print "preparing to execute func1....."
		print "........"
		print "executed...."
	
class contact(object):
	def __init__(self):
		self.phoneNumber = 201
		
			
class enterInfo(contact):
	def __init__(self,a):
		contact.__init__(self)
		self.name = a
	def getName(self):
		return self.name
	def getNumber(self):
		return self.phone_number
	def getAllAttributes(self):
		return self.phoneNumber, self.name

