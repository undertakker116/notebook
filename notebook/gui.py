# gui.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from contact import Contact, AddressBook


class AddressBookApp(App):

    def build(self):
        self.address_book = AddressBook()
        layout = BoxLayout(orientation='vertical')

        # Поля ввода
        self.name_input = TextInput(hint_text='Имя', multiline=False)
        self.surname_input = TextInput(hint_text='Фамилия', multiline=False)
        self.number_input = TextInput(hint_text='Номер телефона', multiline=False)
        self.extra_number_input = TextInput(hint_text='Дополнительный номер', multiline=False)
        self.notes_input = TextInput(hint_text='Заметки', multiline=False)

        # Кнопки
        add_button = Button(text='Добавить контакт')
        add_button.bind(on_press=self.add_contact)

        show_button = Button(text='Показать все контакты')
        show_button.bind(on_press=self.show_contacts)

        # Добавление виджетов в макет
        layout.add_widget(self.name_input)
        layout.add_widget(self.surname_input)
        layout.add_widget(self.number_input)
        layout.add_widget(self.extra_number_input)
        layout.add_widget(self.notes_input)
        layout.add_widget(add_button)
        layout.add_widget(show_button)

        return layout

    def add_contact(self, instance):
        contact = Contact(
            name=self.name_input.text,
            surname=self.surname_input.text,
            number=self.number_input.text,
            extra_number=self.extra_number_input.text,
            notes=self.notes_input.text
        )
        self.address_book.add_contact(contact)

    def show_contacts(self, instance):
        for contact in self.address_book.contacts:
            print(contact)


if __name__ == "__main__":
    AddressBookApp().run()
