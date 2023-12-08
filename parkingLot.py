import json
import boto3

class ParkingSpot:
    def __init__(self):
        self.car = None

class ParkingLot:
    def __init__(self, square_footage, parking_spot_size = 96):
        self.square_footage = square_footage
        self.parking_spot_size = parking_spot_size
        self.spots = []  # Initialize as an empty list
        for _ in range(self.calculate_spots()):
            self.spots.append(ParkingSpot())  # Add ParkingSpot objects to the list
        self.parked_cars = {}

    def calculate_spots(self):
        return int(self.square_footage / self.parking_spot_size)

    def is_spot_empty(self, spot_number):
        return self.spots[spot_number].car is None

    def park_car(self, car, spot_number):
        self.spots[spot_number].car = car
        self.parked_cars[car.license_plate] = spot_number

    def to_json(self):
        parked_cars_json = {}
        for license_plate, spot_number in self.parked_cars.items():
            parked_cars_json[license_plate] = spot_number + 1
        return json.dumps(parked_cars_json)

    def upload_to_s3(self, filename):
        # Connect to S3
        s3_client = boto3.client('s3')

        # Define bucket and key
        bucket_name = "parking_lot_bucket"
        file_key = filename

        # Upload file to S3 bucket
        with open(filename, 'rb') as f:
            s3_client.upload_fileobj(f, bucket_name, file_key)

        print(f"Successfully uploaded parked cars data to S3: s3://{bucket_name}/{file_key}")

    def save_parked_cars_data(self, filename):
        parked_cars_json = self.to_json()

        with open(filename, 'w') as f:
            f.write(parked_cars_json)

        print(f"Parke cars data saved to file: {filename}")