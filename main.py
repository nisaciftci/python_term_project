from file_manager import load_data
from user import register_user, login_user
from bank_operations import deposit, withdraw, transfer
from report import generate_report, export_history

def main():
    print(" ~ Welcome to NisaBank ~ ")
    
    users = load_data()

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Admin Report")
        print("4. Exit")

        choice = input("Choose (1-4): ")

        if choice == "1":
            name = input("Username: ")
            pw = input("Password: ")
            register_user(users, name, pw)

        elif choice == "2":
            name = input("Username: ")
            pw = input("Password: ")
            
            if login_user(users, name, pw):
                while True:
                    print(f"\n Welcome {name}!")
                    print(f"Balance: {users[name]['balance']} TL")
                    print("1. Deposit Money")
                    print("2. Withdraw Money")
                    print("3. Transfer Money")
                    print("4. View History")
                    print("5. Export History (txt)")
                    print("6. Logout")

                    sub_choice = input("Choose (1-6): ")

                    if sub_choice == "1":
                        amt = input("Amount to deposit: ")
                        deposit(users, name, amt)

                    elif sub_choice == "2":
                        amt = input("Amount to withdraw: ")
                        withdraw(users, name, amt)

                    elif sub_choice == "3":
                        target = input("Receiver username: ")
                        amt = input("Amount to transfer: ")
                        transfer(users, name, target, amt)

                    elif sub_choice == "4":
                        print("\nTransaction History: ")
                        for record in users[name]["history"]:
                            print("-" + record)

                    elif sub_choice == "5":
                        export_history(name, users[name]["history"]) 

                    elif sub_choice == "6":
                        print("Logging out...")
                        break
        
        elif choice == "3":
            admin_pass = input("Admin Password: ")
            if admin_pass == "1234":
                generate_report(users)
            else:
                print("Wrong password!")

        
        elif choice == "4":
            print("Goodbye...")
            break
main()













