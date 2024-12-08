class person(object):

    def __init__(self,name,age):
        self.name = name
        self.age  = age

    def info (self):
        print(self.name)
        print(self.age)

class employ(person):

    def __init__(self, name, age , address):
       self.address = address

       person. __init__(self , name , age)


e =employ("Hanzla" , 11 , "Lucknow")
e.info()
    