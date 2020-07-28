class A():
    count = 0
    def __init__(self):
        A.count += 1

    def exclaim(self):
        print("I'm an A!")

    @classmethod
    def kid(cls):
        print("A has ", cls.count, "little objects")

    @staticmethod
    def describe_A():
        print("A Class Static Methods")
