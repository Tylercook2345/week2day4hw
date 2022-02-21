
class Cart():
    def __init__(self, items):
        self.items = items 

    def addtoyourCart(self):    
        items=input("What would you like to add to your cart?")
        self.items.append(items)

    def showCart(self):
        for items in self.items:
            print(items)

    def deletefromCart(self):
        for items in self.items:
            self.items.remove(items)

    shoppingCart = ([])

def run():
        while True:
            response = input("What would you like to do? add/show/remove or quit? ")
        
            if response.lower() == "quit":
                Cart.showCart()
                print("Have a great day!")
                break

            elif response.lower() == "add":
                Cart.addtoyourCart()
            
            elif response.lower() == "show":
                Cart.showCart()

            elif response.lower() == "remove":
                print("The last item was taken out of your cart")
                Cart.deletefromCart()
            else: 
                print("invalid input, please choose from one of these options (add/show/remove or quit)")
            
run()


            


