class product:
    def __init__(self,name,price,stock_quailty):
        self.name=name
        self.price=price
        self.stock_quailty=stock_quailty

    def upadte_stock(self,quantity):
        self.stock_quailty -=quantity
        
    def display_product(self):
        return f"{self.name}: ${self.price}, Stock: {self.stock_quantity}"
    
class shoppingcart:
    def __init__(self,cart):
        self.cart=cart
    
    def add_product(self,product,quan):
        if product.stock_quailty >= quan:
            self.cart.append({product,quan})
            product.upadte_stock(quan)
            print(f'{product.name} added to cart {quan}')
        else:
            print(f'not avaible{product.name}')
    
    def cal(self):
        total=sum(item["product"].price * item["quan"]
                for item in  self.cart )
        return total
        


p1=product('laptop',50000,10)
s1=shoppingcart()

class Product:
    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def update_stock(self, quantity):
        self.stock_quantity -= quantity

    def display_product(self):
        return f"{self.name}: ${self.price}, Stock: {self.stock_quantity}"

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_product(self, product, quantity):
        if product.stock_quantity >= quantity:
            self.cart.append({"product": product, "quantity": quantity})
            product.update_stock(quantity)
            print(f"{product.name} added to cart (Quantity: {quantity})")
        else:
            print(f"Not enough stock for {product.name}")

    def calculate_total(self):
        total = sum(item["product"].price * item["quantity"] for item in self.cart)
        return total

    def checkout(self):
        print(f"Total Cart Value: ${self.calculate_total()}")
        self.cart.clear()
        print("Checkout Successful!")

# Example Usage
product1 = Product("Laptop", 50000, 10)
product2 = Product("Phone", 30000, 5)

cart = ShoppingCart()
cart.add_product(product1, 2)  # Adding 2 laptops
cart.add_product(product2, 1)  # Adding 1 phone

cart.checkout()
