import utils
path = "data/products.json"
# ====================================================
#                    PRODUCTS
# ====================================================
def add_products():
    # this function adds products

    product_list = utils.load_file(path)
    name = input("enter product name: ")
    category = input("enter product category: ")
    price = int(input("enter product price: "))
    stock = int(input("enter product stock: "))
    product_list.append({
            'id': int(max(item['id'] for item in product_list) + 1),
            'name': name,
            'category': category,
            'price': price,
            'stock': stock
    })
    utils.save_file(path, product_list)

def remove_products():
    product_list = utils.load_file(path)
    id = int(input("Enter product id: "))
    name = input("Enter product name: ")
    for item in product_list:
        if item["id"] == id and item["name"] == name:
            product_list.remove(item)
    utils.save_file(path, product_list)

def edit_products():
    # this function edits products
    product_list = utils.load_file(path)
    looking_for_id = int(input("enter product id: "))
    looking_for_name = input("enter product name: ")
    id = int(input("enter product id: "))
    name = input("enter product name: ")
    category = input("enter product category: ")
    price = int(input("enter product price: "))
    stock = int(input("enter product stock: "))
    for item in product_list:
        if looking_for_id == item["id"] and looking_for_name == item["name"]:
             item.update({"id": id, "name": name, "category": category, "price": price, "stock": stock})
    utils.save_file(path, product_list)

def search_products_by_name():
    # this function searches products by their name
    product_list = utils.load_file(path)
    name = input("enter product name: ")
    print(utils.search("name", name, product_list))

def search_products_by_category():
    # this function searches products by their category
    product_list = utils.load_file(path)
    category = input("enter product category: ")
    items = utils.search("category", category, product_list)
    print(items)

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