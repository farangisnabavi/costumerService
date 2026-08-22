import json

def load_file(path):
    #loads json file
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("file not found, try again")
    else:
        print("something went wrong, try again")

def save_file(path, data):
    #saves json file
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        print("file not found, try again")
    else:
        print("something went wrong, try again")

def search(column, value, file):
    #searches items
    items = []
    for item in file:
        if item[column] == value:
            items.append(item)
    return items
