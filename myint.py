class MyInt:
		def __init__(self, original_object = 0):
				self.value = int(original_object)

		def __str__(self):
				return "MyInt object with value: " + str(self.value)


		# object of square.
		def square(self):
				ret_obj = MyInt(self.value * self.value)
				return ret_obj
				

a = MyInt(6.2)
print(a)
b = MyInt(5)
print(b)
c = MyInt(3)
print(c)

d = a.square()

print(a,"The square root calculated is:",d)

print(d == 25)

