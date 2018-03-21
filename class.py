class baseclass():
	def method1(self):
		print "base method1"

class derivedclass(baseclass):
	def method1(self):
		baseclass.method1(self)
		print "derived -method1"

class main():
	d=derivedclass()
	d.method1()
	

if __name__=="__main__":
		main()
