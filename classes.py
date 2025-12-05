from collections import UserDict
from datetime import date
from utils import date_to_string, str_to_date, adjust_for_weekend

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not self.validate(value):
            raise ValueError("Phone number must contain exactly 10 digits")
        super().__init__(value)
    
    @staticmethod
    def validate(value):
        return value.isdigit() and len(value) == 10

class Birthday(Field):
    def __init__(self, value):
        self.text = None
        try:
            self.value = str_to_date(value)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        
    def replace(self, old_text, new_text):
        self.text = self.text.replace(old_text, new_text)
        return self.text

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]
    
    def edit_phone(self, old_phone, new_phone):
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return
        raise ValueError(f"Phone number {old_phone} not found")
    
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None
    
    def add_birthday(self, day):
        self.birthday = Birthday(day)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
    
    def get_upcoming_birthdays(self, days=7):
        upcoming_birthdays = []
        today = date.today()

        for user in self.data.values():
            if user.birthday is None:
                continue
            birthday_date = user.birthday.value.date()
            birthday_this_year = birthday_date.replace(year=today.year)
            if (birthday_this_year - today).days < 0:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                
            if 0 <= (birthday_this_year - today).days <= days:
                congratulation_date_str = date_to_string(adjust_for_weekend(birthday_this_year))
                upcoming_birthdays.append({"name": user.name.value, "congratulation_date": congratulation_date_str})
        return upcoming_birthdays
    
    def __str__(self):
        if not self.data:
            return "Address book is empty"
        return "\n".join(str(record) for record in self.data.values())
