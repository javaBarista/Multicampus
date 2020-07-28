class Person():
    def __init__(self, name):
        self.name = name
    def language(self):
        pass

class Eartling(Person):
    def language(self, language):
        return language

class Groot(Person):
    def language(self, language):
        return language

name = ['Jejudo', 'Dr.Strange', 'Groot']
country = ['Korea', 'USA', "Galaxy"]
language = ['Korean', 'English', "unKnown"]


for idx, name in enumerate(name):
    if country[idx].upper != 'GALAXY':
        person = Eartling(name)
        print(person.language(language[idx]))
    else :
        groot = Groot(name)
        print(groot.language(language[idx]))
