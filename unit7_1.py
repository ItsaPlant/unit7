# class Car:
#    def __init__(self, make, model_name, top_speed, colour):
#        self.make = make
#        self.model_name = model_name
#        self.top_speed = top_speed
#        self.color = colour
    
#     # def __str__(self):
#     #     return f"{self.color} {self.make} {self.model_name}"

# # print(mustang)
# # print(mustang.make)


class Person:
    def __init__(self, name, surname, company, position, mail):
        self.name = name
        self.surname = surname
        self.company = company
        self.position = position
        self.mail = mail

        #Variables
        self.current_speed = 0

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __repr__(self):
        return f"""REPR
        name = {self.name}
        surname = {self.surname}
        company = {self.company}
        position = {self.position}
        mail = {self.mail}"""

    def __eq__(self, other):
        return all(
            (
                self.name == other.name,
                self.surname == other.surname,
                self.company == other.company,
                self.position == other.position,
                self.mail == other.mail
            )
        )
    
    def __gt__(self, other):
        return self.position > other.position

    def accelerate(self, step = 10):
        self.current_speed += step
    
    def decelerate(self, step=10):
        self.current_speed -= step

    def contact(self):
        return f"I contact with {self.name} {self.surname}"

    





personas = []

P1 = Person(name = "Karolina", surname = "Wysocka", company="Alpha Beta", position = 64, mail="KarolinaWysocka@dayrep.com")
P2 = Person(name = "Karolina", surname = "Wysocka", company="Alpha Beta", position = 50397, mail="KarolinaWysocka@dayrep.com")
P3 = Person(name = "Karolina", surname = "Wysocka", company="Alpha Beta", position = 875, mail="KarolinaWysocka@dayrep.com")
P4 = Person(name = "Karolina", surname = "Wysocka", company="Alpha Beta", position = 987, mail="KarolinaWysocka@dayrep.com")
P5 = Person(name = "Karolina", surname = "Wysocka", company="Alpha Beta", position = 345, mail="KarolinaWysocka@dayrep.com")

personas.extend([P1, P2, P3, P4, P5])
print(personas)

for person in personas:
    print(person.name, person.surname, person.surname, person.company, person.position, person.mail)

print(dir(P1))

print(P1)

print(P1 < P2)

by_pos = sorted(personas, key = lambda person: person.position)
print(P1.contact)