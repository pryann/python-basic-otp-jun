# def fetch_items(items):
#     return items


def find_item(item_id, items):
    for item in items:
        if item["id"] == item_id:
            return item


def create_item(create_payload, items):
    # new_id = items[-1]["id"] + 1
    # new_id = max(item["id"] for item in items) + 1
    items.append(create_payload)
    return items[-1]


def update_item(item_id, update_payload, items):
    item = find_item(item_id, items)
    if item is not None:
        index = items.index(item)
        items[index].update(update_payload)
        return items[index]


def remove_item(item_id, items):
    item = find_item(item_id, items)
    items.remove(item)
