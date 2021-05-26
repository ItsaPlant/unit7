class Person:
    def __init__(self, name, surname, company, position, mail):
        self.name = name
        self.surname = surname
        self.company = company
        self.position = position
        self.mail = mail

        #var

        self._name_len = 0

    

    def __str__(self):
        return f"{self.name} {self.surname}"

    # def __repr__(self):
    #     return f"""REPR
    #     name = {self.name}
    #     surname = {self.surname}
    #     company = {self.company}
    #     position = {self.position}
    #     mail = {self.mail}"""

    def __eq__(self, other = 10):
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

    def contact(self):
        print(f"I contact with {self.name} {self.surname}")

    @property
    def name_len(self):
        return self._name_len

    @name_len.setter          ################SETTER NIE DZIAŁA
    def name_len(self, value = 10):
        name = len(self.name)
        surname = len(self.surname)
        lenght = (name + surname + 1)
        self._name_len = lenght
        

P1 = Person(name = "Karolina", surname = "Wysocka", company="Alpha Beta", position = 64, mail="KarolinaWysocka@dayrep.com")
P2 = Person(name = "Karolina", surname = "Wysocka", company="Alpha Beta", position = 50397, mail="KarolinaWysocka@dayrep.com")
P3 = Person(name = "Karolina", surname = "Wysocka", company="Alpha Beta", position = 875, mail="KarolinaWysocka@dayrep.com")
P4 = Person(name = "Karolina", surname = "Wysocka", company="Alpha Beta", position = 987, mail="KarolinaWysocka@dayrep.com")
P5 = Person(name = "Karolina", surname = "Wysocka", company="Alpha Beta", position = 345, mail="KarolinaWysocka@dayrep.com")

P1.contact()
# print(P1.name_len)
#print(len(P1.name))

P1.name_len = 10
to_print = P1.name_len

print(to_print)
