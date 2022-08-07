from datetime import datetime

import Constant

# Helps Encapuslate a "Truck" by creating a truck model
#Values such as speed, current payload and other tracking metrics are built into the truck class
class Truck:
    def __init__(self, start_time):
        #print("Truck Class")
        self.speed = Constant.SPEED
        self.payload = []
        self.curr_location = Constant.START_LOCATION
        self.payload_limit = Constant.PACKAGE_LIMIT
        self.trip_total = 0
        self.elapsed_time = 0
        self.start_time = start_time
        self.last_package_delivery = self.start_time
        self.total_time_in_min = 0
        self.end_time = 0

