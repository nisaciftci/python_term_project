def main_menu():
    print("\n Banking Management System")
    print("1. Login")
    print("2. Register")
    print("3. Exit")

    choice = input("Please select an option (1-3): ")
    return choice

def start_program():
    while True:
        choice = main_menu()

        if choice == "1":
            print("Redirecting to Login...")
            #login kod eklenecek

        elif choice == "2":
            print("Redirecting to Registration...")
            #registration code eklenecek

        elif choice == "3":
            print("Exiting the system...")
            break 

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    start_program()
    
