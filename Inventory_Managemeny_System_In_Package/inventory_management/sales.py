from .inventory import inventory_data, check_stock

def sell_item(item_name, quantity):
    """Sell an item and update inventory."""
    if item_name not in inventory_data or inventory_data[item_name] < quantity:
        print(f"Error: Not enough stock for {item_name}.")
        return False
    inventory_data[item_name] -= quantity
    print(f"Sold {quantity} of {item_name}.")
    return True