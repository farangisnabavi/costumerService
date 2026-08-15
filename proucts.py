import utils
path = "data/products.json"
# ====================================================
#                    PRODUCTS
# ====================================================
def add_products(id, name, category, price, stock):
    # this function adds products
    with open("data/products.json", 'a', encoding='utf-8') as f:
        product_list = utils.load_file(path)
    product_list.append({
            'id': id,
            'name': name,
            'category': category,
            'price': price,
            'stock': stock
    })
    utils.save_file(path, product_list)

def remove_products(id, name):
    # this function deletes products
    product_list = utils.load_file(path)
    for item in product_list:
        if id in item['id'] and name in item['name']:
            product_list.remove(item)
    utils.save_file(path, product_list)

def edit_products(id, name, category, price, stock, looking_for_id, looking_for_name):
    # this function edits products
    product_list = utils.load_file(path)
    for item in product_list:
        if looking_for_id in item['id'] and looking_for_name in item['name']:
             item.update({"id": id, "name": name, "category": category, "price": price, "stock": stock})
    utils.save_file(path, product_list)

def search_products_by_name(name):
    # this function searches products by their name
    product_list = utils.load_file(path)
    for item in product_list:
        if name in item['name']:
            print("id: ", item['id'], "\nname: ", item['name'], "\ncategory: ", item['category'], "\nprice: ",
                 item['price'], "\nstock: ", item['stock'])


def search_products_by_category(category):
    # this function searches products by their category
    product_list = utils.load_file(path)
    for item in product_list:
        if category in item['category']:
            print("id: ", item['id'], "\nname: ", item['name'], "\ncategory: ", item['category'], "\nprice: ",
                      item['price'], "\nstock: ", item['stock'])


def show_products():
    # this function prints products
    product_list = utils.load_file(path)
    for item in product_list:
        print("id: ", item['id'], "\nname: ", item['name'], "\ncategory: ", item['category'], "\nprice: ",
                item['price'], "\nstock: ", item['stock'])


def sort_by_price():
    # this function sortes by price
    product_list = utils.load_file(path)
    print(sorted(product_list, key=lambda x: x["price"]))


def sort_by_stock():
    # this function sortes by stock
    product_list = utils.load_file(path)
    print(sorted(product_list, key=lambda x: x["stock"]))