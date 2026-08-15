import utils
path = "data/users.json"
# ====================================================
#                    COSTUMERS
# ====================================================
def add_costumer():
    # this function adds costumers
    costumer_list = utils.load_file(path)
    name = input("enter your costumer name: ")
    phone = input("enter your phone: ")
    city = input("enter your city: ")
    vip = input("enter if vip: ")
    costumer_list.append({
            'id': max(item['id'] for item in costumer_list) + 1,
            'name': name,
            'phone': phone,
            'city': city,
            'vip': vip
    })
    utils.save_file(path, costumer_list)

def remove_costumers():
    # this function deletes costumers
    costumer_list = utils.load_file(path)
    name = input("enter your costumer name to remove: ")
    id = input("enter your costumer id: ")
    for item in costumer_list:
        if id in item['id'] and name in item['name']:
            costumer_list.remove(item)
    utils.save_file(path, costumer_list)

def edit_costumers():
    # this function edits users
    costumer_list = utils.load_file(path)
    looking_for_id = input("enter your costumer id: ")
    looking_for_name = input("enter your costumer name: ")
    id = input("enter your costumer id: ")
    name = input("enter your costumer name: ")
    phone = input("enter your phone: ")
    city = input("enter your city: ")
    vip = input("enter if vip: ")
    for item in costumer_list:
        if looking_for_id in item['id'] and looking_for_name in item['name']:
            item.update({"id": id, "name": name, "phone": phone, "city": city, "vip": vip})
    utils.save_file(path, costumer_list)

def show_costumers():
    # this function prints users
    costumer_list = utils.load_file(path)
    for item in costumer_list:
         print("id: ", item['id'], "\nname: ", item['name'], "\nphone: ", item['phone'], "\ncity: ",
                item['city'], "\nvip: ", item['vip'])

def search_costumers():
    # this function searches users by their name
    costumer_list = utils.load_file(path)
    name = input("enter your costumer name: ")
    print(utils.search("name",name,costumer_list))