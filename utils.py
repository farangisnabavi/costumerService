#====================================================
#                    PRODUCTS
#====================================================
def add_products(id,name,category,price,stock):
    #this function adds products
    with open(data/products.json, 'a', encoding='utf-8') as productList:
        productList.append({
            'id': id,
            'name': name,
            'category': category,
            'price': price,
            'stock': stock
        })
def remove_products(id, name):
    #this function deletes products
    with open(data/products.json, 'rw', encoding='utf-8') as productList:
       for item in productList:
           if id in item['id'] and name in item['name']:
               productList.remove(item)
def edit_products(id, name, category, price, stock, looking_for_id, looking_for_name):
   #this function edits products
    with open(data/products.json, 'rw', encoding='utf-8') as productList:
        for item in productList:
            if looking_for_id in item['id'] and looking_for_name in item['name']:
                item.update({"id": id, "name": name, "category": category, "price": price, "stock": stock})
def search_products_by_name(name):
    #this function searches products by their name
    with open(data/products.json, 'r', encoding='utf-8') as productList:
        for item in productList:
            if name in item['name']:
                print("id: ", item['id'],"\nname: ",item['name'],"\ncategory: ", item['category'],"\nprice: ", item['price'],"\nstock: ", item['stock'])
