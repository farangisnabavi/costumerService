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

def print_total():
    # prints totals
    order_list=utils.load_file(path)
    name = input("Enter costumer name: ")
    items= utils.search("costumer", name, order_list)
    for item in items:
        print(item["id"], item["costumer"], item["products"],item["total"])

def delete_order():
    #deletes orders
    orders_list=utils.load_file(path)
    id = input("Enter order id: ")
    for i in orders_list:
        if i["id"] == int(id):
            orders_list.remove(i)
    utils.save_file(path, orders_list)