# ================ Modules ================

from visuals import logo, home_menu, hm2, loading
from data import menu, resources
import os
import time

wallet = 0
password = "coffee"
coffee = ""

# ================ Administration functions ================

def report(resources):
    print(f"\n💧 Water : {resources["water"]} ml.\n🐄 Milk : {resources["milk"]} ml.\n☕ Coffee : {resources["coffee"]} g.\n")
    print(f"\nCurrent earnings: {wallet} CZK.")
    input("\nOK ")
    os.system("cls")
    ui()

def refill(resources, logo, home_menu):
    if resources["water"] == 400 or resources["milk"] == 300 or resources["coffee"] == 150:
        os.system("cls")
        print(logo)
        print(home_menu)
        print("\n⚠️  Resources already full.")
        time.sleep(2)
        os.system("cls")
        ui()
    
    resources["water"] = 400
    resources["milk"] = 300
    resources["coffee"] = 150
    print(f"\n💧 Water : {resources["water"]} ml.\n🐄 Milk : {resources["milk"]} ml.\n☕ Coffee : {resources["coffee"]} g.\n")
    print("\n✅ Successfully refilled.")
    time.sleep(2)
    os.system("cls")
    ui()

# ================ Function that handles money ================

def coins():

    print("Insert coins 1/2/5/10/20/50")
    money = input("> ").split(" ")
    money_in = 0
    if money == str:
        print("❌ Invalid input. Please insert coins.")
        time.sleep(2)
        os.system("cls")
        ui()

    for i in money:
        money_in += int(i)

    if money_in <= 0:
        print("❌ Cannot insert negative or zero amount.")
        time.sleep(2)
        os.system("cls")
        ui()

    return money_in

# ================ Coffee preparing function, handles resources, =========================
# ================ choices and side scenarios such as lack of ingredients =================

def main(menu, resources, choice):
    global wallet

    if choice == "1":
    
        i = "espresso"
        cost = 40

    elif choice == "2":
    
        i = "cappuccino"
        cost = 60

    elif choice == "3":
    
        i = "latte"
        cost = 50
    
    else:
        print("❌ Invalid choice.")
        time.sleep(2)
        os.system("cls")
        ui()

    if resources["water"] < menu[i]["ingredients"]["water"] or resources["milk"] < menu[i]["ingredients"]["milk"] or resources["coffee"] < menu[i]["ingredients"]["coffee"]:
        print("❌ Cannot make your drink due to lack of ingredients.")
        time.sleep(3)
        os.system("cls")
        ui()

    os.system("cls")
    print(logo)
    hm2(choice)
    print(f"Insert {menu[i]["cost"]} CZK.")
    money_in = coins()

    if money_in == 5:
        print("\nCancelled")
        time.sleep(1)
        os.system("cls")
        ui()

    if money_in < menu[i]["cost"]:

        print("❌ Insufficient funds.")
        time.sleep(2)
        os.system("cls")
        ui()

    wallet += cost

    for item in menu[i]["ingredients"]:
        resources[item] -= menu[i]["ingredients"][item]

    loading()
    print("Your drink is ready ✅ Be careful, it's hot. ☕")

    if money_in > menu[i]["cost"]:
        money_back = money_in - menu[i]["cost"]
        print(f"Change: {money_back} CZK.")

    time.sleep(5)
    os.system("cls")
    ui()

# ================ Main menu (User Interface) program ================

def ui():
    print(logo)
    print(home_menu)

    choice = input("> ")

    if choice == "4":
        print("\nEnter the number of drink that you want\n\nFor admins: report - current state of the resources and profit\n            refill - refill resources\n            off - turns of the machine")
        input("OK ")
        os.system("cls")
        ui()
        
    elif choice == "report":
        input_password = input("Password: ")
        if password == input_password:
            report(resources)
        
        else: 
            print("\n❌ No administration access.")
            time.sleep(2)
            os.system("cls")
            ui()
        
    
    elif choice == "refill":
        input_password = input("Password: ")
        if password == input_password:
            refill(resources, logo, home_menu)

        else: 
            print("\n❌ No administration access.")
            time.sleep(2)
            os.system("cls")
            ui()
        

    elif choice == "off":
        input_password = input("Password: ")
        if password == input_password:
            print("\nShutting down...")
            time.sleep(1)
            exit()

        else: 
            print("\n❌ No administration access.")
            time.sleep(2)
            os.system("cls")
            ui()

    main(menu, resources, choice)

ui()
