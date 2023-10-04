#!/usr/bin/env python3

class Person:
    pass
    # Class body goes here
    def _init_(self, talk, walk):
        self.talk=talk
        self.walk=walk
        
        
    def talk(self):
        print("Hello World!")
        return "Hello World!"
    
    def walk(self):
        print("The person is walking.")
        return "The person is walking."

    
person1 = Person()
# person2 = Person()

print(person1.talk())
print(person1.walk())
# print(person2.talk())
        

