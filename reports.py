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