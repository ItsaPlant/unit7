from faker import Faker
fake = Faker()

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

    @name_len.setter          
    def name_len(self, value = 10):
        name = len(self.name)
        surname = len(self.surname)
        lenght = (name + surname + 1)
        self._name_len = lenght
        
class BasicContact(Person):
    def __init__(self, name, surname, mail, phone):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.mail = mail
        #var
        self._label_len = 0

    def __repr__(self):
        return f"""
        CONTACT
        name = {self.name}
        surname = {self.surname}
        phone = {self.phone}
        mail = {self.mail}"""

    def call(self):
        print(f"calling{self.name} {self.surname}, private number {self.phone}")

    @property
    def label_len(self):
        self.label_len = "XDD"
        return self._label_len

    @label_len.setter
    def label_len(self, value = 10):
        self._label_len = (len(self.name) + len(self.surname) + 1)

class BusinessContact(Person):
    def __init__(self, phone, work_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.phone = phone
        self.work_phone = work_phone

    def __repr__(self):
        return f"""
        CONTACT
        name = {self.name}
        surname = {self.surname}
        phone = {self.work_phone}
        mail = {self.mail}"""
    
    def call(self):
        print(f"calling{self.name} {self.surname}, work number {self.work_phone}")

    @property
    def label_len(self):
        self.label_len = "XDD"
        return self._label_len

    @label_len.setter
    def label_len(self, value = 10):
        self._label_len = (len(self.name) + len(self.surname) + 1)

def create_cards(type, quantity):
    """1 is Basic 2 is Business"""
    _contact_list = []
    if type == 1:
        for _ in range(quantity):#BASIC
            nam_sur = fake.name()
            nam_sur = nam_sur.split(" ")
            name = nam_sur[0]
            surname = nam_sur[1]
            phone = fake.phone_number()
            mail = fake.ascii_free_email()

            contact = BasicContact(name, surname, mail, phone)
            _contact_list.append(contact)

    elif type == 2:#BUSINESS
        for _ in range(quantity):
            nam_sur = fake.name()
            nam_sur = nam_sur.split(" ")
            name = nam_sur[0]
            surname = nam_sur[1]
            work_phone = fake.phone_number()
            mail = fake.ascii_free_email()
            company = fake.company()
            position = fake.bs()

            contact = BusinessContact(name = name, surname = surname, company = company, position = position, mail = mail, phone = work_phone, work_phone = work_phone)
            _contact_list.append(contact)

    return _contact_list


P1 = BasicContact(name = "Karolina", surname = "Wysocka", phone = "123 666 677", mail="KarolinaWysocka@dayrep.com")
P2 = BusinessContact(name = "Karolina", surname = "Wysocka", company="Alpha Beta", position = 50397, phone = "123 666 677", work_phone = "+23 876 235 536", mail="KarolinaWysocka@dayrep.com")
P3 = Person(name = "Karolina", surname = "Wysocka", company="Alpha Beta", position = 875, mail="KarolinaWysocka@dayrep.com")
# P4 = Person(name = "Karolina", surname = "Wysocka", company="Alpha Beta", position = 987, phone = "123 666 677", work_phone = "+23 876 235 536", mail="KarolinaWysocka@dayrep.com")
# P5 = Person(name = "Karolina", surname = "Wysocka", company="Alpha Beta", position = 345, phone = "123 666 677", work_phone = "+23 876 235 536", mail="KarolinaWysocka@dayrep.com")


to_print = P1.label_len

print(to_print)

to_print2 = P2.label_len

print(to_print2)

contact_list =create_cards(2, 3)
print(contact_list)