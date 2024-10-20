CUSTOMERS = [
    {
        "id": 1,
        "name": "Ryan Tanay"
    }
]

# Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found animal, if it exists
    requested_location = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_location = customer

    return requested_location

def get_all_customers():
  return CUSTOMERS