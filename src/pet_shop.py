# WRITE YOUR FUNCTIONS HERE

# Test 1 - return the name of the pet shop
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

# Test 2 - return the total cash held at the moment
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# Tests 3 & 4 - add or remove cash from the till - does not return a value
def add_or_remove_cash(pet_shop,cash_value):
    pet_shop["admin"]["total_cash"] += cash_value

# Test 5 - return the number of pets sold that day
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

# Test 6 - increase the number of pets sold - does not return a value
def increase_pets_sold(pet_shop, num_pets_sold):
    pet_shop["admin"]["pets_sold"] += num_pets_sold

# Test 7 - return the level of stock
def get_stock_count(pet_shop):
    # print(len(pet_shop["pets"]))
    return len(pet_shop["pets"])

