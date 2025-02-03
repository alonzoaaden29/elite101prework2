print("Welcome to Aaden's Bank Account Helper Chatbot!")
name = input("What is your name? ")
age = input("Hello " + name + ", how old are you?")
print("Awesome!, What kind of account would you like to open?")

#From youtube - Andy Dolinski
def menu():
    print("[1] Checkings Account")
    print("[2] Savings Account")
    print("[3] Retirement Account")
    print("[4] Health Savings Account")
    print("[3] More Help")
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

