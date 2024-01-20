# Product Class: Represents a product with name, price, and category attributes
class Product:
    def __init__(self, name, price, category):
        # Initialize product attributes
        self._name = name
        self._price = price
        self._category = category

    # Define how products are classified
    def __eq__(self, other): 
         # Check if name, price, and category are equal for two products
         if isinstance(other, Product):
             if  ((self._name == other._name and self._price == other._price) and (self._category==other._category)):
                return True
             else:
                return False
         else:
            return False

    def get_name(self):#gets the name of the product
        return self._name

    def get_price(self):#gets the price of the product
        return self._price

    def get_category(self):#gets the category of the product
        return self._category

    # Implement string representation
    def __repr__(self):
        rep = 'Product(' + self._name + ',' + str(self._price) + ',' + self._category + ')'
        return rep
    
# Inventory Class: Manages a dictionary of products with their price and quantity
class Inventory:
    def __init__(self):# Initialize an empty inventory dictionary
        self._inventory={}


    # Add a product to the inventory
    def add_to_productInventory(self,productName,productPrice,productQuantity):
        self._inventory[productName]={"price":productPrice,"quantity":productQuantity}
    
    # Add quantity to a product in the inventory
    def add_productQuantity(self,nameProduct,addQuantity):
       if nameProduct in self._inventory:
            self._inventory[nameProduct]["quantity"]+=(addQuantity)

    # Remove quantity from a product in the inventory
    def remove_productQuantity(self,nameProduct,removeQuantity):
        if nameProduct in self._inventory:
            self._inventory[nameProduct]["quantity"]-=removeQuantity

    # Get the price of a product from the inventory
    def get_productPrice(self,nameProduct):
        return self._inventory[nameProduct]["price"]

    # Get the quantity of a product from the inventory
    def get_productQuantity(self,nameProduct):
        return self._inventory[nameProduct]["quantity"]

    #Display the products and their details in the inventory
    def display_Inventory(self):
        for product, details in self._inventory.items():
            print(f"{product}, {details['price']}, {details['quantity']}")

                      
# ShoppingCart Class: Represents a shopping cart for a buyer
class ShoppingCart:
    # Initialize shopping cart with buyer name, an empty cart, and an inventory
    def __init__(self,buyerName,inventory):
        self._buyerName=buyerName
        self._cart={}
        self._inventory=inventory

    # Add a product to the shopping cart with a requested quantity
    def add_to_cart(self,nameProduct,requestedQuantity):
        if self._inventory.get_productQuantity(nameProduct) >= requestedQuantity:
            if nameProduct in self._cart:
                self._cart[nameProduct]+= requestedQuantity
            else:
                self._cart[nameProduct]=requestedQuantity

            self._inventory.remove_productQuantity(nameProduct,requestedQuantity)
            return "Filled the order"
        else:
            return"Can not fill the order"
    
    # Remove a product from the shopping cart  with a requested quantity
    def remove_from_cart(self,nameProduct,requestedQuantity):
        if nameProduct not in self._cart:
            return"Product not in the cart"
        else:
            if requestedQuantity>self._inventory.get_productQuantity(nameProduct):
                return"The requested Quantity to be removed from the cart exceeds what is in the cart"
            else:
                self._cart[nameProduct]-=requestedQuantity
                self._inventory.add_productQuantity(nameProduct,requestedQuantity)
                return"Successful"
    # View the contents of the shopping cart with the total price and buyer name
    def view_cart(self):
        total=0
        for product, quantity in self._cart.items():
            price=self._inventory.get_productPrice(product)
            total+=price*quantity
            print(f"{product} {quantity}")
        print(f"Total:{total}")
        print(f"Buyer Name: {self._buyerName}")


# ProductCatalog Class: Manages a catalog of products
class ProductCatalog:
    # Initialize an empty catalog and sets for different price categories
    def __init__(self):
        self._catalog=[]
        self._low_prices=set()
        self._medium_prices=set()
        self._high_prices=set()

    # Add a product to the catalog
    def addProduct(self, product):
        self._catalog.append(product)

    # Categorize products based on their prices
    def price_category(self):
        for product in self._catalog:
            if 0 <= product.get_price() <= 99:
                self._low_prices.add(product._name)
            elif 100 <= product.get_price() <= 499:
                self._medium_prices.add(product.get_name())
            else:
                self._high_prices.add(product.get_name())

        print(f"Number of low price items: {len(self._low_prices)}")
        print(f"Number of medium price items: {len(self._medium_prices)}")
        print(f"Number of high price items: {len(self._high_prices)}")

    # Display the product catalog
    def display_catalog(self):
        for product in self._catalog:
            print(f"Product: {product.get_name()} Price: {product.get_price()} Category: {product.get_category()}")    


    # Function to populate inventory from a file
def populate_inventory(filename):
    inventory=Inventory()

    openfile=open(filename,"r")
    for line in openfile.readlines():
        if line.strip() != "":
            info = line.strip().split(",")
            inventory.add_to_productInventory(info[0],int(info[1]),int(info[2]))
    return inventory
    # Function to populate product catalog from a file
def populate_catalog(fileName):
    productCatalog = ProductCatalog()

    openfile=open(fileName,"r")
    for line in openfile.readlines():
        if line.strip() != "":
            info = line.strip().split(",")
            product = Product(info[0],int(info[1]),info[3])
            productCatalog.addProduct(product)
    return productCatalog
    





        


  


            


