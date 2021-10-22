# WRITE YOUR FUNCTIONS HERE

# return the name of the pet shop
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

# return the total cash held at the moment
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# add or remove cash from the till - does not return a value
def add_or_remove_cash(pet_shop,cash_value):
    pet_shop["admin"]["total_cash"] += cash_value

