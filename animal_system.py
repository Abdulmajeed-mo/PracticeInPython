# نظام حيوانات 🐾

from abc import ABC ,abstractmethod

#Parent Class
class Animal (ABC) :
    def __init__ (self ,name):
        self.__name=name
   
    @abstractmethod
    def speak (self) :
        pass
    
    #Getter
    def get_name(self):
       return self.__name


#Child Class
class Dog (Animal):
    def speak(self):
        print("Dog Sound")


#call
dog =Dog("naruto")
dog.speak ()
print(dog.get_name())


    

   



