print("Welcome to the food ordering Chatbot")
name = input("What is your name? ")
age = input("Hello " + name + ", how old are you?")
print("Awesome!, how may i help you?")

def menu():
    print("[1] Option 1")
    print("[2] Option 2")
    print("[0] Exit program")


menu()
option = int(input("Enter your option:"))

while option !=0:
    if option == 1:
        print("Option 2 has been called.")
    elif option == 2:
        print("Option 2 has been called.")
    else:
        print("Invalid option.")

        print()
        menu()
        option = int(input("Enter your option: "))


print("Thanks for using this program. Adios!")

