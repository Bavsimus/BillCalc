import items


def main():
    orders = []
    varorders = []
    tea = items.drink('Tea', 'drink', 5, 'hot')
    fries = items.item('Fries', 'food', 10)
    icecream = items.item("Ice Cream", "dessert", 2)
    coffee = items.drink('Coffee', 'drink', 5, 'hot')
    menu = [tea, fries, icecream, coffee]
    print("+------------------------------+")
    print("Welcome to BillCalc by Bavsimus!")
    print("+  Type bill to calculate      +")
    print("+------------MENU--------------+")
    for k in range(0, len(menu)):
        print(k+1, ".", menu[k].get_name(), "| ", menu[k].get_price(), "$")
    order = 0
    index = 0
    while order != "bill":
        orders.append(order)
        order = input("Enter the order: ")
        index += 1
    orders.remove(0)
    for i in range(0, len(orders)):
        for j in range(0, len(menu)):
            if menu[j].get_name() == orders[i]:
                varorders.append(menu[j])
    total = 0
    for k in range(0, len(varorders)):
        total += varorders[k].get_price()
    for t in range(0, len(varorders)):
        print("----------------------------")
        print(t+1, ".", varorders[t].get_name(), "| ", varorders[t].get_price(), "$")
    print("----------------------------")
    print("                Total: ", total, "$")
    print("----------------------------")


main()
