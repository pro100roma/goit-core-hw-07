from classes import AddressBook
from functions import parse_input, add_contact, change_contact, show_phone, add_birthday, show_birthday, birthdays, show_all

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