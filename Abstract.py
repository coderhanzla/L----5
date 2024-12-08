from abc import ABC

class hobbies(ABC):
    def hobbies(self):
        pass

class Hanzla(hobbies):
    def hobbies(self):
        print("My Hobby is to do coding")

class Anaf(hobbies):
     def hobbies(self):
         print("My Hobby is to play Foot Ball")

class Arsh(hobbies):
     def hobbies(self):
         print("My Hobby is to play Volley Ball")

h= Hanzla()
h.hobbies()

an = Anaf()
an.hobbies()

ar = Arsh()
ar.hobbies()

