from datetime import datetime

import Package
import Addresses
import Constant

class Truck:
    def __init__(self, leave_time):
        print("Truck Class")
        self.speed = Constant.SPEED
        self.payload = []
        self.curr_location = Constant.START_LOCATION
        self.payload_limit =Constant.PACKAGE_LIMIT
        self.trip_total = 0
        self.miles_at_timedate = 0
        self.start_time = datetime.combine(datetime.today().date(), datetime.strptime(leave_time, "%H:%M").time())
        self.end_time = ''
        self.leave_time = leave_time
        self.last_package_delivery = self.leave_time

    def deliver_packages(self):
        print("Package Delivery!")
        for package_id in self.payload:
            #package[Constant.STATUS] = 'In Transit'
            package = Package.obj.getPackage(package_id)
            self.curr_location = package[Constant.ADDRESS]
            #self.last_package_delivery = 
            print(package)

    def minDistanceFrom(self, fromAddress, truckPackages):
        # Loop through, find minimum distance
        distances = []
        for package in truckPackages:
            distances[Addresses.distanceBetween(fromAddress, package.address)] = package.id
        
        return distances.sort()[0] # return shortest distance

    def load(self, packages):

        for package_id in packages:
            package = Package.HashTable.lookup(package_id)
            print(package)
            package.status = 'Loaded at HUB'
            self.payload.append(package)
        print("Truck Loaded!")
