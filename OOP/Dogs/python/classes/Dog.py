class Dog:
	_breed = str(); #Variables with one underscore "_" are protected
	_color = str();
	_sleeping = False;
	_weight = int();
	_timesBarked = int();
	name = str();

	def __init__(self, name, breed, color, weight):
		self.name = name;
		self._breed = breed;
		self._color = color;
		self._weight = weight;

	def bark(self):
		if self._sleeping == False:
			if self._timesBarked >= 4:
				self._sleeping = True;
				print('woof!');
			else:
				print('woof!');
				self._timesBarked += 1;
		else:
			print("The dog is sleeping!");

	def dogInfo(self):
		print('Dog Breed:', self._breed);
		print('Dog Color:', self._color);
		print('Dog Weight:', self._weight);
		print('Dog Name:', self.name);


class SmallDog(Dog):
	scared = True;

	def __init__(self, name, breed, color, weight):
		super(SmallDog, self).__init__(name, breed, color, weight);
		if weight > 15:
			print("That is a big dog!");

	def bark(self):
		if self._sleeping == False:
			if self.scared == True:
				print("The dog is scared, try to pet it");
			else:
				if self._timesBarked >= 4:
					self._sleeping = True
					print("Yip!");
				else:
					print("Yip!");
					self._timesBarked += 1;
		else:
			print("The dog is sleeping..");

	def pet(self):
		self.scared = False;

