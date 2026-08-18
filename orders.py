from operator import truediv

import utils
path = "data/orders.json"

def add_order():
    # this function added projects
    orders_list=utils.load_file(path)
    id = max(item['id'] for item in orders_list) + 1
    costumer = input("Enter your costumer: ")
    flag = True
    order_list = []
    while flag:
        product = input("Enter product name: ")
        number = int(input("Enter product number: "))
        price = int(input("Enter product price: "))
        order_list.append({"product" : product, "number" : number, "price" : price})
        yn = input("Would you like to add another order? (y/n): ")
        if yn == "n":
            flag = False
    total = 0
    for i in order_list:
        total += i["price"] * i["number"]
    orders_list.append({"id" : id, "costumer" : costumer, "products" : order_list, "total" : total})
    utils.save_file(path, orders_list)
