class Person:
    def __init__(self, name):
        self.name = name
        self.father = None
        self.mother = None

if __name__ == "__main__":
    child = Person("Abinaya")
    child.father = Person("Ramasamy")
    child.mother = Person("Lakshmi")

    print("Child:", child.name)
    print("Father:", child.father.name)
    print("Mother:", child.mother.name)
