inventory_data = {}

def add_item(item_name, quantity):
    """Add items to the inventory."""
    if item_name in inventory_data:
        inventory_data[item_name] += quantity
    else:
        inventory_data[item_name] = quantity
    print(f"Added {quantity} of {item_name} to inventory.")

def check_stock(item_name):
    """Check the stock of an item."""
    quantity = inventory_data.get(item_name, 0)
    print(f"Stock of {item_name}: {quantity}")
    return quantity