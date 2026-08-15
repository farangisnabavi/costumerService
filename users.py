import json

# ====================================================
#                    COSTUMERS
# ====================================================
def add_costumer(id, name, phone, city, vip):
    # this function adds costumers
    with open("data/users.json", 'a', encoding='utf-8') as f:
        costumer_list = json.load(f)
    costumer_list.append({
            'id': id,
            'name': name,
            'phone': phone,
            'city': city,
            'vip': vip
    })
    with open("data/users.json", 'w', encoding='utf-8') as f:
        json.dump(costumer_list, f, ensure_ascii=False, indent=4)

def remove_costumers(id, name):
    # this function deletes costumers
    with open("data/users.json", 'rw', encoding='utf-8') as f:
        costumer_list = json.load(f)
    for item in costumer_list:
        if id in item['id'] and name in item['name']:
            costumer_list.remove(item)
    with open("data/users.json", 'w', encoding='utf-8') as f:
        json.dump(costumer_list, f, ensure_ascii=False, indent=4)

def edit_costumers(id, name, phone, city, vip, looking_for_id, looking_for_name):
    # this function edits users
    with open("data/users.json", 'rw', encoding='utf-8') as f:
        costumer_list = json.load(f)
        for item in costumer_list:
            if looking_for_id in item['id'] and looking_for_name in item['name']:
                item.update({"id": id, "name": name, "phone": phone, "city": city, "vip": vip})
        json.dump(costumer_list, f, ensure_ascii=False, indent=4)

def show_costumers():
    # this function prints users
    with open("data/users.json", 'r', encoding='utf-8') as f:
        costumer_list = json.load(f)
        for item in costumer_list:
            print("id: ", item['id'], "\nname: ", item['name'], "\nphone: ", item['phone'], "\ncity: ",
                  item['city'], "\nvip: ", item['vip'])

def search_costumers(name):
    # this function searches users by their name
    with open("data/users.json", 'r', encoding='utf-8') as f:
        costumer_list = json.load(f)
        for item in costumer_list:
            if name in item['name']:
                print("id: ", item['id'], "\nname: ", item['name'], "\ncphone ", item['phone'], "\ncity: ",
                      item['city'], "\nvip: ", item['vip'])