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

# Test 6 - increase the number of pets sold - does not return anything
def increase_pets_sold(pet_shop, num_pets_sold):
    pet_shop["admin"]["pets_sold"] += num_pets_sold

# Test 7 - return the level of stock
def get_stock_count(pet_shop):
    # print(len(pet_shop["pets"]))
    return len(pet_shop["pets"])

# Test 8 & 9 - find names of pets by breed
def get_pets_by_breed(pet_shop, pet_breed):
    pet_name=[]

    for each_pet in pet_shop["pets"]:
        if each_pet["breed"] == pet_breed:
            pet_name.append(each_pet["name"])

    return pet_name

# Test 10 & 11 - find a pet by it's name, return a dictionary of the pet
# what if there is more than one pet with the same name? Possibly return a list, but test wouldn't work for that
def find_pet_by_name(pet_shop, pet_name):
    for each_pet in pet_shop["pets"]:
        if each_pet["name"] == pet_name:
            return each_pet

# Test 12 - remove a pet from the list, returns after the first match
def remove_pet_by_name(pet_shop, pet_name):
    each_pet_index=0

    for each_pet in pet_shop["pets"]:
        if each_pet["name"] == pet_name:
            pet_shop["pets"].pop(each_pet_index)
            return
        
        each_pet_index += 1

# Test 13 - add a pet to the stock, does not return anything
def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

# Test 14 - return the amount of cash a customer has, return an integer
def get_customer_cash(customer):
    return customer["cash"]

# Test 15 - reduce customer cash by an amount, does not return anything
def remove_customer_cash(customer, cash_value):
    customer["cash"] -= cash_value

# Test 16 - get the number of pets a customer has, return an integer
def get_customer_pet_count(customer):
    return len(customer["pets"])

# Test 17 - add a pet to a customer, no return value
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

# Test 18 - customer has sufficient funds
def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False

    