EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis"
    }
]

# Function with a single parameter
def get_single_employee(id):
    # Variable to hold the found animal, if it exists
    requested_location = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_location = employee

    return requested_location

def get_all_emplyees():
  return EMPLOYEES