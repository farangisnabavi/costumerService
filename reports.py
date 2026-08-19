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
