def add_products(id,name,category,price,stock):
    with open(data/products.json, 'a', encoding='utf-8') as productList:
        productList.append({
            'id': id,
            'name': name,
            'category': category,
            'price': price,
            'stock': stock
        })
