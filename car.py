class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        return f"Car with license plate {self.license_plate}"

    def park(self, parking_lot, spot_number):
        if not parking_lot.is_spot_empty(spot_number):
            return "Car was not parked successfully. Spot already occupied."
        parking_lot.park_car(self, spot_number)
        return f"Car with license plate {self.license_plate} parked successfully in spot {spot_number}"