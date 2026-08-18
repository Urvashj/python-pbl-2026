module_code = '''
def product_details(name, price):
    return "Product: " + name + ", Price: " + str(price)

def category(item):
    return "Category: " + item
'''

with open("product_info.py", "w") as file:
    file.write(module_code)

import product_info

print(product_info.product_details("Keyboard", 850))
print(product_info.category("Computer Accessory"))