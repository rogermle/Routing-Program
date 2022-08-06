# Roger Le
# C950 Performance Assessment
# Student ID: 1060770

from Package import Package
from Truck import Truck
import csv
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import time
from HashTable import HashTable

# Package Constants

ID = 0
ADDRESS = 1
CITY = 2
STATE = 3
ZIP_CODE = 4
DUE_DATETIME = 5
WEIGHT = 6
NOTES = 7
STATUS = 8
DELIVERY_START_TIME = 9

AT_HUB_STATUS = "AT HUB"

# Truck Constants
START_LOCATION = '4001 South 700 East'
SPEED = 18
MINUTES_PER_HOUR = 60
SECONDS_PER_MIN = 60
PACKAGE_LIMIT = 16

# Reads the csv files(desinations) and creates a dictionary from raw data to unique IDs for usage on the algorithm below.
distanceData = 'csv/distances.csv'
addressData = 'csv/addresses.csv'
distance_dict = {}
address_dict = {}

# Time Complexity O(N)
# Space Complexity O(N)
def loadAddressData(addressData):
    with open(addressData) as addressCSV:
        addresses = list(csv.reader(addressCSV, delimiter=','))
        for address in addresses:
            address_dict[address[2].strip()] = address[0]
    # print(address_dict)


# Read distance and address CSV files
# Time Complexity O(N^2)

def loadDistanceData(distanceData):
    with open(distanceData) as distanceCSV:
        distances = list(csv.reader(distanceCSV, delimiter=','))
        for col, distance1 in enumerate(distances):
            for row, distance2 in enumerate(distances):
                index = f'{col}{row}'
                # Special Case for the HUB
                if distances[col][row] == '0.0':
                    distance_dict[index] = '0.0'
                    break;
                # Reverse Lookup, Prevents having to handle in code
                # If from and to address are reversed, return same distance
                rev_index = f'{row}{col}'
                distance_dict[index] = distances[col][row]
                distance_dict[rev_index] = distances[col][row]
    # print(distance_dict)


def distanceBetween(fromAddress, toAddress):
    try:
        return distance_dict[f'{address_dict[fromAddress]}{address_dict[toAddress]}']
    except:
        print("Error Condition: Invalid Address")

loadAddressData(addressData)
loadDistanceData(distanceData)

packageHashTable = HashTable()

today = datetime.now()

def main():
    print(f"Today is {today}")
    print("Welcome to WGU Package Delivery")
    print("\r\n")
    print("Please select one of the following options:")
    print("\r\n")
    print("Package Look up by ID Press 1")
    print("All Packages by Time in HH:MM format Press 2")
    print("Exit Application Press 3")

    choice = input("Please enter a valid number: ")

    if (choice == "1"):
        #print("Package Lookup")
        id = input("Please enter a valid package ID (1-40): ")
        pretty_print_package(id)
    elif (choice == "2"):
        print("Date Time Lookup")
        time = input("Please enter a time after 08:00:00 to search package statuses (in military time e.g 0900): ")



        print(time)
    elif (choice == "3"):
        exit()
    else:
        main()


def pretty_print_package(id):
    package = packageHashTable.lookup(int(id))
    print(
        f' ID: {package.id} | Address: {package.address} | City: {package.city} | Zip: {package.zip_code} | Due Date: {package.due_datetime} | Weight: {package.weight} | Status: {package.status} | Delivery Time: {package.delivery_time.strftime("%I:%M %p")}')


def print_all_packages(time):
    print("Packages at {time}: \r\n")


def loadPackages():
    # import data from CSV into HashTable
    global packageHashTable
    with open('csv/packages.csv') as packages_file:
        csv_reader = csv.reader(packages_file, delimiter=',')
        for data in csv_reader:
            id = data[0]
            address = data[1]
            city = data[2]
            state = data[3]
            zip_code = data[4]
            due_datetime = data[5]
            weight = data[6]
            notes = data[7]
            status = "AT HUB"
            delivery_time = ''
            # Create Package object
            package = Package(id, address, city, state, zip_code, due_datetime, weight, notes)

            packageHashTable.insert(int(id), package)
    print("Packages Loaded")


def deliver_packages(truck):
    truck.elapsed_time = 0.0
    delivery_distance_matrix = {}
    #print("Package Delivery!")
    # Get Closest Package and then deliver packages

    for package_id in range(len(truck.payload)):
        package = truck.payload[package_id]
        package.status = "En Route"
        delivery_distance_matrix[package.id] = distanceBetween(truck.curr_location, package.address)

    for delivery_pair in range(len(delivery_distance_matrix)):
        keys = list(delivery_distance_matrix.keys())
        values = list(delivery_distance_matrix.values())
        closest_package_index = int(values.index(min(values)))

        closest_package = truck.payload[closest_package_index]

        truck.trip_total += values[closest_package_index]
        truck.elapsed_time += values[closest_package_index]/SPEED
        truck.curr_location = closest_package.address
        #print(closest_package)
        closest_package.status = "Delivered"
        closest_package.delivery_time = datetime.combine(datetime.today().date(), datetime.strptime(truck.start_time, '%H:%M').time()) + timedelta(hours=truck.elapsed_time)
        #Update Global
        packageHashTable.insert(closest_package.id, closest_package)
        pretty_print_package(closest_package.id)
        #print(truck.trip_total)
        truck.payload.remove(closest_package)
        del delivery_distance_matrix[keys[closest_package_index]]

        # Update distance matrix location after each delivery
        for package in range(len(truck.payload)):
            next_package = truck.payload[package]
            delivery_distance_matrix[next_package.id] = distanceBetween(truck.curr_location, next_package.address)

    if len(truck.payload) == 0:
        truck.trip_total += distanceBetween(truck.curr_location, START_LOCATION)
        truck.curr_location = START_LOCATION
        truck.end_time = datetime.combine(datetime.today().date(), datetime.strptime(truck.start_time, '%H:%M').time()) + timedelta(hours=truck.elapsed_time)
        print("Returned to HUB!")

def distanceBetween(fromAddress, toAddress):

    try:
        return float(distance_dict[f'{address_dict[fromAddress]}{address_dict[toAddress]}'])
    except:
        print("Error Condition: Invalid Address")

def loadTruck(truck, packages):
    for package_id in packages:
        package = packageHashTable.lookup(int(package_id))
        #print(package)
        package.status = 'Loaded at HUB'
        truck.payload.append(package)
    #print("Truck Loaded!")


loadPackages()
# print(packageHashTable.lookup(33))

truck1 = Truck('08:05')
truck2 = Truck('09:15')
truck3 = Truck('10:20')

# Package to Adjust Address

addressChange = packageHashTable.lookup(9)
addressChange.address = "410 S State St"
addressChange.zip_code = "84111"

payload1 = [13, 39, 27, 35, 4, 40, 20, 21, 19, 14, 15, 16, 34, 29, 1]
payload2 = [3, 8, 30, 18, 36, 37, 38, 5, 12, 23, 11, 10, 31, 32, 6]
payload3 = [28, 2, 33, 7, 17, 22, 24, 25, 26, 9]

loadTruck(truck1, payload1)
loadTruck(truck2, payload2)
loadTruck(truck3, payload3)

deliver_packages(truck1)
deliver_packages(truck2)
deliver_packages(truck3)

total_truck_miles = truck1.trip_total + truck2.trip_total + truck3.trip_total
#total_elapsed_time = truck1.elapsed_time + truck2.elapsed_time + truck3.elapsed_time

print(f"Total Trip Miles: {round(total_truck_miles, 2)}")
#print(f"Total Trip Time: {total_elapsed_time}")

main()
