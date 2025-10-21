#Exmple of program usung python
def greet():
    print("Hello, welcome to the cart calculater!")
    print("Add items to your cart and get the total amount.")

def get_item():
    items = []
    prices = []

    print("\n Adding items...")
    while True:
        item = input("Enter item name (or type 'done' to finish): ")
        if item.lower() == 'done' or item == '':
            break
        price = float(input(f"Enter price for {item}: "))
        items.append(item)
        prices.append(price)
    return items, prices

def calculate_total(prices):
    #return sum(prices) or
    total = 0
    for price in prices:
        total += price
    return total

def check_budget(total):
    budget = float(input("Enter your budget: "))
    if total > budget:
        print(f"Total amount ${total:.2f} exceeds your budget of ${budget:.2f}.")
    else:
        print(f"Total amount ${total:.2f} is within your budget of ${budget:.2f}.")
        print("You can proceed to checkout!")
        print("The reamining budget is ${:.2f}.".format(budget - total))

def dispaly_cart(items, prices, total):
    print("\nYour Cart:")
    if items == 0:
        print("Your cart is empty.")
    else:
        for item in items:
            print(f"- {item}")
        for price in prices:
            print(f"  Price: ${price:.2f}")
        print(f"Total Amount: ${total:.2f}")

def main():
    greet()
    items, prices = get_item()
    total = calculate_total(prices)
    dispaly_cart(items, prices, total)
    check_budget(total)

agian = True
while agian:
    main()
    choice = input("Do you want to shop again? (yes/no): ")
    if choice.lower() == "yes" or choice.lower() == "y":
        agian = True
    else:
        agian = False
        print("Thank you for using the cart calculator. Goodbye!")
