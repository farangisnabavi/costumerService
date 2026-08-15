import utils
path = "data/users.json"
# ====================================================
#                    COSTUMERS
# ====================================================
def add_costumer(id, name, phone, city, vip):
    # this function adds costumers
    costumer_list = utils.load_file(path)
    costumer_list.append({
            'id': id,
            'name': name,
            'phone': phone,
            'city': city,
            'vip': vip
    })
    utils.save_file(path, costumer_list)

def remove_costumers(id, name):
    # this function deletes costumers
    costumer_list = utils.load_file(path)
    for item in costumer_list:
        if id in item['id'] and name in item['name']:
            costumer_list.remove(item)
    utils.save_file(path, costumer_list)

def edit_costumers(id, name, phone, city, vip, looking_for_id, looking_for_name):
    # this function edits users
    costumer_list = utils.load_file(path)
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

def search_costumers(name):
    # this function searches users by their name
    costumer_list = utils.load_file(path)
    name = input("enter your costumer name: ")
    print(utils.search("name",name,costumer_list))