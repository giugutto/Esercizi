class Restaurant:
    def __init__(self, restaurant_name,cuisine_type, number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant_name(self):
        print(f"Nome ristorante: {self.restaurant_name}, Tipo di cucina: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")
    
    def set_number_served(self, new_number):
        self.number_served = new_number
    
    def increment_number_served(self, add_number):
        self.number_served = self.number_served + add_number
