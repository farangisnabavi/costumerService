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