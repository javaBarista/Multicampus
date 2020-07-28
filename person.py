class Person:
    def __init__(self, name):
        self.name = name

class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name

class JDPerdon(Person):
    def __init__(self, name):
        self.name = "lawyer " + name

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email
