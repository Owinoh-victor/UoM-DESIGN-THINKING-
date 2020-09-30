#!/usr/bin/env python3

from classes.Dog import Dog

bark = str();
running = "yes"

d = Dog("max", "lab", "black", 90);
d.dogInfo();
while running == "yes":
	bark = input("Do you want the dog to bark? (yes/no) --> ")
	if bark == "yes":
		d.bark();
	running = input("Again? (yes/no) --> ");