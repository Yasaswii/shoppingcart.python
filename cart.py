from products import products
cart=[]
max_items=8
def view_products(products):
    print("Available Products:")
    for product in products:
        print(f"ID:{product} {product["name"]}-{product["price"]}")
    print()

def add_to_cart(products,cart,product_id,quantity):
    if len(cart)>=max_items:
        print("cart is full cannot add more items")
        return
    for product in products:
        if product["id"]==product_id:
            for item in cart:
                if item["id"]==product_id:
                    item["quantity"]+=quantity
                    print(f"updated{product["name"]} quantity to {item["quantity"]}")
                    return
            cart.append({"id": product["id"], "name": product["name"], "price": product["price"], "quantity": quantity})
            print(f" {product['name']} added to cart (Qty: {quantity})")
            return
    print("product not found")

def view_cart(cart):
    if not cart:
        print("cart is empty")
        return
    print("Your cart items:")
    total=0
    for item in cart:
        item_total=item["price"]*item["quantity"]
        total+=item_total
        print(f"{item['name']} | ₹{item['price']} x {item['quantity']} = ₹{item_total}")

    print(f"Total Amount = ₹{total}")

def update_cart(cart,product_id,quantity):
    for item in cart:
        if item["id"]==product_id:
            item["quantity"]=quantity
            print(f"updated {item["name"]}quantity to {quantity}")
            return
    print("item not found in cart")

def remove_from_cart(cart,product_id):
    for item in cart:
        if item["id"]==product_id:
            cart.remove(item)
            print(f"removed {item["name"]}from cart")
            return
    print("item not found in cart")

def checkout(cart):
    if not cart:
        print("cart is empty")
    view_cart(cart)
    print("Checkout is complete")
    cart.clear()





                
                
               





