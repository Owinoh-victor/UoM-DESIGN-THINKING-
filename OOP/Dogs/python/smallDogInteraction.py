#!/usr/bin/env python3

from classes.Dog import SmallDog;

bark = str();
running = "yes";

sd = SmallDog("Brian", "chiwawa", "tan", 6);
sd.dogInfo();
while running == "yes":
	bark = input('Do you want the dog to bark? (yes/no/pet) --> ');
	if bark == "yes":
		sd.bark();
	elif bark == "pet":
		sd.pet();
	running = input('Again? (yes/no) --> ');