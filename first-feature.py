# The objective of this module is to calculate the total of items in shopping cart
import json
import ijson

shopping_cart = 'cart.json'
coupon_file = 'coupons.json'
tax_rate = 0.0825

def loading_shopping_cart(shopping_cart):
    try:
        with open(shopping_cart, "r") as file:
             cart_data = list(ijson.items(file, "item"))
        return cart_data
    except (FileNotFoundError, json.JSONDecodeDataError):
        return None

def loading_coupon_data(coupon_file):
    try: 
        with open(coupon_file, "r") as file:
             coupon_data = list(ijson.items(file, "item"))
        return coupon_data 
    except (FileNotFoundError, json.JSONDecodeDataError):
        return None

#cart_data, coupon_data
def calculate_grand_total(cart_data, coupon_data, tax_rate):
    sub_total = 0
    
    for item in cart_data:
        sub_total += item["price"]
    for item in cart_data:
        sku = item["sku"]
        for coupon in coupon_data:
            if sku == coupon["appliedSku"]:
               sub_total -= coupon["discountPrice"]
    tax_total = sub_total * tax_rate
    grand_total = sub_total + tax_total
    
    g_total = '%.2f'%grand_total
    return g_total
 
#g_total =  
if cart_data is not None and coupon_data is not None:
   g_total = calculate_grand_total(cart_data, coupon_data, tax_rate)
   print("Subtotal: $",g_total)
else:
   print("Cart is empty!")

    
