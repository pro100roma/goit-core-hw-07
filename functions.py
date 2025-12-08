from classes import Record

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter the argument for the command"
        except AttributeError:
            return "Contact not found."
    return inner

def parse_input(user_input):
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args
    except:
        return "Invalid command."

@input_error
def add_contact(args, book):
    name, phone, *birthday = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    if birthday:
        record.add_birthday(birthday[0])
    return message

@input_error
def change_contact(args, book):
    name, old_phone, new_phone, *birthday = args
    record = book.find(name)
    record.edit_phone(old_phone, new_phone)
    if birthday:
        record.add_birthday(birthday[0])
    return "Contact updated."

@input_error
def show_phone(args, book):
    name = args[0]
    record = book.find(name)
    return [phone.value for phone in record.phones]

@input_error
def add_birthday(args, book):
    name, birthday = args
    record = book.find(name)
    if birthday:
        record.add_birthday(birthday)
    return "Contact updated."

@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if record.birthday is None:
        return "Birthday isn't set for this contact"
    return record.birthday

@input_error
def birthdays(book):
    upcoming_birthdays = book.get_upcoming_birthdays()
    return upcoming_birthdays

def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)