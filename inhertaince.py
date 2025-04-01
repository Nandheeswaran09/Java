class vehicle:
    def __init__(self,brand,model,rental_price):
        self.brand=brand
        self.model=model
        self.rental_price=rental_price
    
    def show(self):
        print(f'{self.brand},{self.model},{self.rental_price}')

class car(vehicle):
    def __init__(self, brand, model, rental_price,seating_capacity):
        super().__init__(brand, model, rental_price)
        self.seat=seating_capacity

class bike(vehicle):
    def __init__(self, brand, model, rental_price,helmet):
        super().__init__(brand, model, rental_price)
        self.helmet=helmet
        
    def show(self):
        print("vechile type : bike")
        super().show()
        if self.helmet:
            print('yes')
        else:
            pass

brand_car = input("Enter car brand: ")
model_car = input("Enter car model: ")
rental_price_car = float(input("Enter car rental price per day: "))
seating_capacity = int(input("Enter car seating capacity: "))

brand_bike = input("Enter bike brand: ")
model_bike = input("Enter bike model: ")
rental_price_bike = float(input("Enter bike rental price per day: "))
has_helmet = input("Does the bike have a helmet? (yes/no): ").strip().lower() == 'yes'

# Creating objects
car = car(brand_car, model_car, rental_price_car, seating_capacity)
bike = bike(brand_bike, model_bike, rental_price_bike, has_helmet)

c1.show()
b1.show()
