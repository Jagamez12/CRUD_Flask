from model import Person, lista
import view



def add_person(id, fname, lname):
    Person.add_person(id, fname, lname)

def del_person(id):
    Person.del_person(id)

def start():
    view.app.run()
    print(lista)
    


if __name__ == "__main__":
    # running controller function
    start()
