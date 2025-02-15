from .inventory import inventory_data

def generate_inventory_report():
    """Generate a report of current inventory."""
    print("\nInventory Report:")
    for item, quantity in inventory_data.items():
        print(f"{item}: {quantity}")
    print()