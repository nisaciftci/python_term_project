from file_manager import save_data

def deposit(users, username, amount):
    amount = float(amount)

    if amount <= 0:
        print("Error: Amount must be positive!")
        return
    
    users[username]["balance"] += amount
    users[username]["history"].append(f"Deposited: {amount}")

    save_data(users)
    print("Deposit successful!")

def withdraw(users, username, amount):
    amount = float(amount)

    if amount <= 0:
        print("Error: amount must be positive!")
        return
    
    if users[username]["balance"] < amount:
        print("Error: Insufficient balance!")
        return
    
    users[username]["balance"] -= amount
    users[username]["history"].append(f"Withdrew: {amount}")

    save_data(users)
    print("Withdrawal successful!")

def transfer(users, sender, receiver, amount):
    amount = float(amount)

    if receiver not in users:
        print("Error: Receiver not found!")
        return
    
    if users[sender]["balance"] < amount:
        print("Error: Insufficient balance!")
        return
    
    users[sender]["balance"] -= amount
    users[sender]["history"].append(f"Transfered {amount} to {receiver}")

    users[receiver]["balance"] += amount
    users[receiver]["history"].append(f"Received {amount} from {sender}")

    save_data(users)
    print("Transfer successful!")

    