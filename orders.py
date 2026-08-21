from operator import truediv

import utils
path = "data/orders.json"

def add_order():
    # this function added projects
    orders_list=utils.load_file(path)
    id = int(max(item['id'] for item in orders_list) + 1)
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
    product_list = utils.load_file("data/products.json")
    for i in product_list:
        for j in order_list:
            if j["name"] == i["product"]:
                if not i["stock"] == 0 :
                    j["stock"] -= i["number"]
                else:
                    print("ناموجود")
    utils.save_file("data/products.json", product_list)


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

def orders_per_costumer():
    # searches orders for a costumer
    orders_list=utils.load_file(path)
    costumer = input("Enter costumer name: ")
    items = utils.search("costumer", costumer, orders_list)
    for item in items:
        print(item)
