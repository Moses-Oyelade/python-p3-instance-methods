#!/usr/bin/env python3

class Dog:
    pass 

    # Class body goes here
    def _init_(self, bark, sit):
        self.bark=bark
        self.sit=sit
        
        
    def bark(self):
        print("Woof!")
    
    def sit(self):
        print("The dog is sitting.")
        
dog1 = Dog()
snoopy = Dog()

print(dog1.bark())
print(dog1.sit())
print(snoopy.bark())