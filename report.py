def generate_report(users):
    print("\n ~ BANK SYSTEM REPORT ~ ")

    total_bank_balance = 0
    total_users = 0

    for username in users:
        balance = users[username]["balance"]
        total_bank_balance += balance
        total_users += 1
        print(f"User: {username} | Balance: {balance} TL")

    print("-" * 30)
    print(f"Total Users: {total_users}")
    print(f"Total Money in Bank: {total_bank_balance} TL")
    print("-" * 30)

def export_history(username, history):
    filename = f"{username}_history.txt"
    with open(filename, "w") as file:
        file.write(f"Transaction Historty for {username}\n")
        file.write("=" * 30 + "\n")
        for line in history:
            file.write(line+ "\n")
    print(f"History exported to {filename} successfully.")