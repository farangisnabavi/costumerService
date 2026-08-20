from functools import reduce
import utils
productPath = "data/products.json"
ordersPath = "data/orders.json"
usersPath = "data/users.json"

def stock_worth():
    #calculates the stock worth
    products = utils.load_file(productPath)
    product_stock = []
    product_price = []
    for product in products:
        product_stock.append(product["stock"])
        product_price.append(product["price"])
    stocks_worth = list(map(lambda x,y: x*y, product_stock, product_price))
    final_worth = reduce(lambda x,y: x+y, stocks_worth)
    print(final_worth)

def all_stock():
    #counts the stock
    products = utils.load_file(productPath)
    product_stock = []
    for product in products:
        product_stock.append(product["stock"])
    count = reduce(lambda x,y: x+y, product_stock)
    print(count)

def user_count():
    #counts users
    users = utils.load_file(usersPath)
    count = 0
    for i in users:
        count = count+1
    print(count)

def vip_users_count():
    #counts vip users
    users = utils.load_file(usersPath)
    count = 0
    for i in users:
        if i["vip"]:
            count = count+1
    print(count)

def count_orders():
    # counts orders
    orders = utils.load_file(ordersPath)
    count = 0
    for i in orders:
        count = count+1
    print(count)

def count_unavailable():
    #shows unavailable products
    products = utils.load_file(productPath)
    unavailable = []
    for i in products:
        if i["stock"] == 0:
            unavailable.append(i)
    print(unavailable)

def less_than_5():
    # shows products that their stock is less than 5
    products = utils.load_file(productPath)
    less_than_5 = []
    for i in products:
        if i["stock"] >= 5:
            less_than_5.append(i)
    print(less_than_5)

def average_price():
    #calculates the average price
    products = utils.load_file(productPath)
    prices = []
    for i in products:
        prices.append(i["price"])
    average_price = reduce(lambda x,y: x+y, prices)/len(prices)
    print(average_price)

def count_by_category():
    #counts by category
    products = utils.load_file(productPath)
    categories = {}
    for i in products:
        if i["category"] not in categories:
            categories.update({i["category"]: 0})
    for j in products:
        categories[j["category"]] += 1
    print(categories)

def count_orders_per_user():
    #counts orders for each costumer
    orders = utils.load_file(ordersPath)
    order = {}
    for i in orders:
        if i["user"] not in order:
            order.update({i["user"]: 0})
        else:
            order[i["user"]] += 1
    print(order)

    