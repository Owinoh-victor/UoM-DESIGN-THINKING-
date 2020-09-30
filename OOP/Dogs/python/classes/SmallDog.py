from Dog import Dog;

class SmallDog(Dog):
	scared = True;

	def __init__(self):
		self.name = name;
		self.__breed = breed;
		self.__color = color;
		self.__weight = weight;
		if weight > 15:
			print("That is a big dog!");

	def bark(self):
		if sleeping == False:
			if self.scared == True:
				print("The dog is scared, try to pet it");
			else:
				if self.__timesBarked >= 4:
					self.__sleeping = True
					print("Yip!");
				else:
					print("Yip!");
					self.__timesBarked += 1;
		else:
			print("The dog is sleeping..");

	def pet(self):
		self.scared = False;