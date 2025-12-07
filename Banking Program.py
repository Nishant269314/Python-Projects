is_running = True
balance = 0
loan = 0
def show_balance():
    print("**************************")
    print(f"Your Balance is: {balance}$")
def with_draw():
    global balance
    try:
        print("**************************")
        amount  = int(input("Enter how much you want to withdraw:"))
    except Exception:
        print("**************************")
        print("Invalid")
        return
    if amount>balance:
        print("**************************")
        print("Not enough balance")
    else:
        balance-=amount
        print("**************************")
        print(f"You balance is: {balance}$")
def deposit():
    global balance
    global loan
    try:
        print("**************************")
        amount = int(input("Enter how much you want to deposit:"))
        print("**************************")
    except Exception:
        print("**************************")
        print("Invalid")
        return
    balance += amount
    loan += amount
    print(f"Your balance is: {balance}$")
def show_loan():
    print("**************************")
    print(loan)
while is_running:
    print("**************************")
    print("     Banking Program      ")
    print("**************************")
    print("1.Show balance")
    print("2.Withdraw")
    print("3.Deposit")
    print("4.Show loan")
    print("5.Exit")
    print("**************************")

    choice = input("Enter your choice(1,2,3,4,5):")

    if choice == "1":
        show_balance()

    elif choice == "2":
        with_draw()

    elif choice == "3":
        deposit()

    elif choice == "4":
        show_loan()
    elif choice == "5":
        print("**************************")
        print("       Bye!")
        print("**************************")
    else:
        print("**************************")
        print("Invalid!")
