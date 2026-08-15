import json

def load_file(path):
    #loads json file
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_file(path, data):
    #saves json file
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def search(column, value, file):
    #searches items
    items = []
    for item in file:
        if item[column] == value:
            items.append(item)
    return items