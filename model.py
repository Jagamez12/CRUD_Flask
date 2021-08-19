import json

lista = []

class Person(object):

    def __init__(self, id,first_name=None, last_name=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    # returns Person name, ex: John Doe
    def name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    @classmethod
    # returns all people inside db.txt as list of Person objects
    

    def add_person(self,id, fname, lname):
        newPerson = Person(id, fname, lname)
        lista.append(newPerson)
    
    def del_person(self, id):
        for p in lista:
            if p.self.id == id:
                lista.remove(p)
