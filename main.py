from classes import AddressBook, Record

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
    if record is None:
        raise KeyError
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
    if record is None:
        raise KeyError
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

def chatbot():
    book = AddressBook()
    # record = Record("Roman")
    # record.add_phone("0961111999")
    # record.add_birthday("07.12.1994")
    # book.add_record(record)
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    chatbot()