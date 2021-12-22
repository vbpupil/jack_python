class Person:
    name = ""
    age = 0
    likeLollies = False

    def __init__(self, name,age,lollyinfo):
        self.name = name
        self.age = age
        self.likeLollies = lollyinfo

people = [
    Person("Jack",12,True),
    Person("Dad",41,False),
    Person("Mum",39,True),
]

for person in people:
    print(person.name)
