import json


# ====================================================
#                    PRODUCTS
# ====================================================
def add_products(id, name, category, price, stock):
    # this function adds products
    with open("data/products.json", 'a', encoding='utf-8') as f:
        product_list = json.load(f)
    product_list.append({
            'id': id,
            'name': name,
            'category': category,
            'price': price,
            'stock': stock
    })
    with open("data/products.json", 'w', encoding='utf-8') as f:
        json.dump(product_list, f, ensure_ascii=False, indent=4)


def remove_products(id, name):
    # this function deletes products
    with open("data/products.json", 'rw', encoding='utf-8') as f:
        product_list = json.load(f)
    for item in product_list:
        if id in item['id'] and name in item['name']:
            product_list.remove(item)
    with open("data/products.json", 'w', encoding='utf-8') as f:
        json.dump(product_list, f, ensure_ascii=False, indent=4)


def edit_products(id, name, category, price, stock, looking_for_id, looking_for_name):
    # this function edits products
    with open("data/products.json", 'rw', encoding='utf-8') as f:
        product_list = json.load(f)
        for item in product_list:
            if looking_for_id in item['id'] and looking_for_name in item['name']:
                item.update({"id": id, "name": name, "category": category, "price": price, "stock": stock})
                json.dump(product_list, f, ensure_ascii=False, indent=4)


def search_products_by_name(name):
    # this function searches products by their name
    with open("data/products.json", 'r', encoding='utf-8') as f:
        product_list = json.load(f)
        for item in product_list:
            if name in item['name']:
                print("id: ", item['id'], "\nname: ", item['name'], "\ncategory: ", item['category'], "\nprice: ",
                      item['price'], "\nstock: ", item['stock'])


def search_products_by_category(category):
    # this function searches products by their category
    with open("data/products.json", 'r', encoding='utf-8') as f:
        product_list = json.load(f)
        for item in product_list:
            if category in item['category']:
                print("id: ", item['id'], "\nname: ", item['name'], "\ncategory: ", item['category'], "\nprice: ",
                      item['price'], "\nstock: ", item['stock'])


def show_products():
    # this function prints products
    with open("data/products.json", 'r', encoding='utf-8') as f:
        product_list = json.load(f)
        for item in product_list:
            print("id: ", item['id'], "\nname: ", item['name'], "\ncategory: ", item['category'], "\nprice: ",
                  item['price'], "\nstock: ", item['stock'])


def sort_by_price():
    # this function sortes by price
    with open("data/products.json", 'r', encoding='utf-8') as f:
        product_list = json.load(f)
        print(sorted(product_list, key=lambda x: x["price"]))


def sort_by_stock():
    # this function sortes by stock
    with open("data/products.json", 'r', encoding='utf-8') as f:
        product_list = json.load(f)
        print(sorted(product_list, key=lambda x: x["stock"]))

# ====================================================
#                    COSTUMERS
# ====================================================
def add_costumer(id, name, phone, city, vip):
    # this function adds costumers
    with open("data/users.json", 'a', encoding='utf-8') as f:
        product_list = json.load(f)
    product_list.append({
            'id': id,
            'name': name,
            'phone': phone,
            'city': city,
            'vip': vip
    })
    with open("data/users.json", 'w', encoding='utf-8') as f:
        json.dump(product_list, f, ensure_ascii=False, indent=4)

def remove_costumers(id, name):
    # this function deletes costumers
    with open("data/users.json", 'rw', encoding='utf-8') as f:
        product_list = json.load(f)
    for item in product_list:
        if id in item['id'] and name in item['name']:
            product_list.remove(item)
    with open("data/users.json", 'w', encoding='utf-8') as f:
        json.dump(product_list, f, ensure_ascii=False, indent=4)

def edit_costumers(id, name, phone, city, vip, looking_for_id, looking_for_name):
    # this function edits users
    with open("data/users.json", 'rw', encoding='utf-8') as f:
        product_list = json.load(f)
        for item in product_list:
            if looking_for_id in item['id'] and looking_for_name in item['name']:
                item.update({"id": id, "name": name, "phone": phone, "city": city, "vip": vip})
        json.dump(product_list, f, ensure_ascii=False, indent=4)

def show_costumers():
    # this function prints users
    with open("data/users.json", 'r', encoding='utf-8') as f:
        product_list = json.load(f)
        for item in product_list:
            print("id: ", item['id'], "\nname: ", item['name'], "\nphone: ", item['phone'], "\ncity: ",
                  item['city'], "\nvip: ", item['vip'])

def search_costumers(name):
    # this function searches users by their name
    with open("data/users.json", 'r', encoding='utf-8') as f:
        product_list = json.load(f)
        for item in product_list:
            if name in item['name']:
                print("id: ", item['id'], "\nname: ", item['name'], "\ncphone ", item['phone'], "\ncity: ",
                      item['city'], "\nvip: ", item['vip'])