# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random

from car import Car
from parkingLot import ParkingLot


def main():
    # Set parking lot size
    square_footage = 2000

    # Set parking spot size
    parking_spot_size = 96 # 8x12 feet

    # Create parking lot
    parking_lot = ParkingLot(square_footage, parking_spot_size)

    # Generate random cars
    cars = [Car(f"ABC{random.randint(100000, 999999)}") for _ in range(20)]

    # Park cars
    for car in cars:
        found_spot = False
        while not found_spot:
            spot_number = random.randint(0, parking_lot.calculate_spots() - 1)
            park_status = car.park(parking_lot, spot_number)
            if park_status.startswith("Car"):
                found_spot = True
                print(park_status)

    # Save parked cars to JSON
    parked_cars_json = parking_lot.to_json()

    # Save parked cars data to file
    filename = "parked_cars.json"
    parking_lot.save_parked_cars_data(filename)

    # Upload parked cars data to S3
    parking_lot.upload_to_s3(filename)

    print(f"Parking lot full. Parked cars: {parked_cars_json}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
