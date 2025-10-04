from products import products
from cart import view_products, add_to_cart, view_cart, update_cart, remove_from_cart, checkout
cart=[]
def menu():
    while True:
        print("Shopping Cart Menu:")
        print("1.View Products")
        print("2.Add to Cart")
        print("3.View Cart")
        print("4.Update cart")
        print("5.Remove from cart")
        print("6.Checkout")
        print("7.Exit")
        choice=input("enter your choice:")
        if choice=="1":
            view_products(products)
        elif choice=="2":
            product_id=int(input("enter product id"))
            quantity=int(input("enter Quantity"))
            if quantity<=0:
                print("quantity must be greater than 0")
            else:
                add_to_cart(products,cart,product_id,quantity)

        elif choice=="3":
            view_cart(cart)
        elif choice=="4":
            product_id=int(input("enter product id to update"))
            quantity=int(input("enter new quantity"))
            if quantity<=0:
                print("quantity must be greater than 0")
            else:
                update_cart(cart,product_id,quantity)
        elif choice=="5":
            product_id=int(input("enter product id"))
            remove_from_cart(cart,product_id)
        elif choice=="6":
            checkout(cart)
        elif choice=="7":
            print("Exiting Thankyou for shopping")
            break
        else:
            print("invald choice please try again")





