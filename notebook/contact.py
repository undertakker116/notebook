import json

class Contact:
    def __init__(self, name, surname, number, extra_number, notes):
        '''иницилизирую объкеты моей записной книжки'''
        self.name = name
        self.surname = surname
        self.number = number
        self.extra_number = extra_number
        self.notes = notes

    def __str__(self):
        '''Возвращает строковое представление контакта'''
        return f"{self.name} {self.surname} - {self.number} {self.extra_number}"

    def to_dict(self):
        '''Преобразует контакт в словарь'''
        return {
            "name": self.name,
            "surname": self.surname,
            "number": self.number,
            "extra_number": self.extra_number,
            "notes": self.notes
        }

    @classmethod
    def from_dict(cls, data):
        '''Создает контакт из словаря'''
        return cls(data["name"], data["surname"], data["number"], data["extra_number"], data["notes"])


class AddressBook:
    def __init__(self):
        self.contacts = []
        self.load_data()

    def save_data(self):
        '''Сохраняет все контакты в JSON файл'''
        with open("contacts.json", "w") as file:
            json.dump([contact.to_dict() for contact in self.contacts], file)

    def load_data(self):
        '''Загружает контакты из JSON файла'''
        try:
            with open("contacts.json", "r") as file:
                data = json.load(file)
                self.contacts = [Contact.from_dict(contact_data) for contact_data in data]
        except FileNotFoundError:
            pass

    def add_contact(self, contact):
        '''Добавление контакта в адресную книгу'''
        if isinstance(contact, Contact):
            self.contacts.append(contact)
            self.save_data()

    def find_contact(self, name):
        '''Поиск контакта по имени'''
        return [contact for contact in self.contacts if contact.name == name]

    def remove_contact(self, contact):
        '''Удаление контакта'''
        self.contacts.remove(contact)
        self.save_data()

    def list_contacts(self):
        '''Вывод всех контактов'''
        for contact in self.contacts:
            print(contact)

    def edit_contact(self, name, **kwargs):
        '''Редактирование контакта по имени'''
        contacts = self.find_contact(name)

        if not contacts:
            print('Контакт не найден!')
            return

        contact = contacts[0]

        for key, value in kwargs.items():
            if hasattr(contact, key):
                setattr(contact, key, value)

        self.save_data()
        print(f'Контакт {name} успешно обновлен!')
