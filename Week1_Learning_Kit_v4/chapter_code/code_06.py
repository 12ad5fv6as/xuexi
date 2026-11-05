def add_item(value, items=None):
    if items is None:
        items = []
    items.append(value)
    return items

print(add_item("A"))
print(add_item("B"))
