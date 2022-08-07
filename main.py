# Roger Le
# C950 Performance Assessment
# Student ID: 1060770

import Constant
from Package import Package
from Truck import Truck
import csv
from datetime import datetime
from datetime import timedelta
from HashTable import HashTable
import math

truck_departure_times = ['08:05', '09:15', '10:20']

# Reads the csv files(desinations) and creates a dictionary from raw data to unique IDs for usage on the algorithm below.
distanceData = 'csv/distances.csv'
addressData = 'csv/addresses.csv'
distance_dict = {}
address_dict = {}

#Global Mileage Log at a specific time
distance_at_time = {}

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

# Time Complexity O(1)
# Space Complexity O(n)
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
    print("Press 1 for Package Look up by ID ")
    print("Press 2 for All Packages by Time in HH:MM format ")
    print("Press 3 to Exit Application")

    choice = input("Please enter a valid number: ")

    if (choice == "1"):
        #print("Package Lookup")
        id = input("Please enter a valid package ID (1-40): ")
        try:
            pretty_print_package(id)
        except:
            print("Invalid Package #")
            main()
    elif (choice == "2"):
        #print("Date Time Lookup")
        time = input("Please enter a time after 08:00:00 to search package statuses (in military time e.g 0900): ")
        print_package_at_time(time)
        #print(time)
    elif (choice == "3"):
        exit()
    else:
        main()





def print_package_at_time(time):
    desired_time = datetime.combine(datetime.today().date(), datetime.strptime(time, '%H:%M').time())
    addressChangeTime = datetime.combine(datetime.today().date(), datetime.strptime('10:20', '%H:%M').time())

    if desired_time >= addressChangeTime:
        packageHashTable.lookup(9).address = "410 S State St"
        packageHashTable.lookup(9).zip_code = "84111"
    elif desired_time < addressChangeTime:
        packageHashTable.lookup(9).address = "300 State St"
        packageHashTable.lookup(9).zip_code = "84103"

    mileage_log(time)

    # Range function is Exclusive
    for package_id in range(1, 41):
        package = packageHashTable.lookup(package_id)
        if package_id in payload1:
            start_time = datetime.combine(datetime.today().date(), datetime.strptime(truck_departure_times[0], '%H:%M').time())
            delivery_time = package.delivery_time
        elif package_id in payload2:
            start_time = datetime.combine(datetime.today().date(), datetime.strptime(truck_departure_times[1], '%H:%M').time())
            delivery_time = package.delivery_time
        elif package_id in payload3:
            start_time = datetime.combine(datetime.today().date(), datetime.strptime(truck_departure_times[2], '%H:%M').time())
            delivery_time = package.delivery_time

        #En Route
        if start_time < desired_time < delivery_time:
            print(
                f' ID: {package.id} | Address: {package.address} | City: {package.city} | Zip: {package.zip_code} | Due Date: {package.due_datetime} | Weight: {package.weight} | Status: En Route'
            )
        # Delivered
        elif desired_time >= delivery_time:
            print(
                f' ID: {package.id} | Address: {package.address} | City: {package.city} | Zip: {package.zip_code} | Due Date: {package.due_datetime} | Weight: {package.weight} | Status: {package.status} | Delivery Time: {package.delivery_time.strftime("%I:%M:%S %p")}'
            )
        # At Hub
        else:
            print(
                f' ID: {package.id} | Address: {package.address} | City: {package.city} | Zip: {package.zip_code} | Due Date: {package.due_datetime} | Weight: {package.weight} | Status: At HUB'
            )

def pretty_print_package(id):
    package = packageHashTable.lookup(int(id))
    print(
        f' ID: {package.id} | Address: {package.address} | City: {package.city} | Zip: {package.zip_code} | Due Date: {package.due_datetime} | Weight: {package.weight} | Status: {package.status} | Delivery Time: {package.delivery_time.strftime("%I:%M:%S %p")}'
    )


# Time Complexity O(N)
# Space Complexity O(1)
# Reads from global mileage log and determines a total
def mileage_log(time):
    desired_time =  datetime.combine(datetime.today().date(), datetime.strptime(time, '%H:%M').time())

    total_mileage = 0
    for delivery_time in distance_at_time:
        if delivery_time <= desired_time:
            total_mileage += distance_at_time[delivery_time]
        else:
            break

    print(f'Total Truck Mileage at {desired_time} is {round(total_mileage, 2)} miles')


def loadPackages():
    # import data from CSV into HashTable
    global packageHashTable
    with open('csv/packages.csv') as packages_file:
        csv_reader = csv.reader(packages_file, delimiter=',')
        for data in csv_reader:
            id = data[Constant.ID]
            address = data[Constant.ADDRESS]
            city = data[Constant.CITY]
            state = data[Constant.STATE]
            zip_code = data[Constant.ZIP_CODE]
            due_datetime = data[Constant.DUE_DATETIME]
            weight = data[Constant.WEIGHT]
            notes = data[Constant.NOTES]
            # Create Package object
            package = Package(id, address, city, state, zip_code, due_datetime, weight, notes)

            packageHashTable.insert(int(id), package)
    #print("Packages Loaded")

# Time Complexity O(N^2)
# Space Complexity O(N^2)
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

        # print(closest_package)
        # Update Truck position, time and distance calculations
        truck.trip_total += values[closest_package_index]
        truck.elapsed_time += values[closest_package_index] / Constant.SPEED
        truck.total_time_in_min += values[closest_package_index] / Constant.SPEED * Constant.SECONDS_PER_MIN
        truck.curr_location = closest_package.address

        arrival_time = datetime.combine(datetime.today().date(),datetime.strptime(truck.start_time, '%H:%M').time()) + timedelta(hours=truck.elapsed_time)
        distance_at_time[arrival_time] = values[closest_package_index]

        # Deliver the Package
        closest_package.status = "Delivered"
        closest_package.delivery_time = arrival_time
        # Update Package Delivery in Global
        packageHashTable.insert(closest_package.id, closest_package)
        pretty_print_package(closest_package.id)

        #print(truck.trip_total)

        # Remove Package from Truck Payload
        truck.payload.remove(closest_package)
        truck.last_package_delivery = arrival_time
        del delivery_distance_matrix[keys[closest_package_index]] # Delete the entry from our Matrix

        # Recalculate next nearest package and update the matrix
        # Update distance matrix location after each delivery
        for package in range(len(truck.payload)):
            next_package = truck.payload[package]
            delivery_distance_matrix[next_package.id] = distanceBetween(truck.curr_location, next_package.address)

    # No More Packages, Return to Base, unless you are truck 3
    # Delivery is done once all packages are delivered
    if len(truck.payload) == 0:
        if truck.start_time == truck_departure_times[2]: # if you the final truck, stop after last delivery
            truck.end_time = datetime.combine(datetime.today().date(), datetime.strptime(truck.start_time, '%H:%M').time()) + timedelta(hours=truck.elapsed_time)
            print(f'Delivery Complete, Truck 3 Located at {truck.curr_location} and abandoned at {truck.end_time} after driving {round(truck.trip_total,2)} miles.')
        else:
            # Return to base code for Truck 1 and Truck 2
            final_distance = distanceBetween(truck.curr_location, Constant.START_LOCATION)
            truck.trip_total += final_distance
            truck.elapsed_time += final_distance / Constant.SPEED
            truck.curr_location = Constant.START_LOCATION
            truck.end_time = datetime.combine(datetime.today().date(),datetime.strptime(truck.start_time, '%H:%M').time()) + timedelta(hours=truck.elapsed_time)
            distance_at_time[truck.end_time] = final_distance
            print(f'Returned to HUB! at {truck.end_time} after driving {round(truck.trip_total,2)} miles!')

def distanceBetween(fromAddress, toAddress):

    try:
        return float(distance_dict[f'{address_dict[fromAddress]}{address_dict[toAddress]}'])
    except:
        print("Error Condition: Invalid Address")

# Time Complexity O(n)
# Space Complexity O(n)
def loadTruck(truck, packages):
    for package_id in packages:
        package = packageHashTable.lookup(int(package_id))
        #print(package)
        package.status = 'Loaded at HUB'
        truck.payload.append(package)
    #print("Truck Loaded!")


loadPackages()
# print(packageHashTable.lookup(33))

truck1 = Truck(truck_departure_times[0])
truck2 = Truck(truck_departure_times[1])
truck3 = Truck(truck_departure_times[2])

# Package to Adjust Address

addressChange = packageHashTable.lookup(9)
addressChange.address = "410 S State St"
addressChange.zip_code = "84111"

payload1 = [1, 35, 27, 39, 4, 40, 19, 20, 21, 14, 15, 16, 34, 29, 13]
payload2 = [3, 5, 30, 18, 36, 37, 38, 8, 11, 23, 12, 10, 32, 31, 6]
payload3 = [2, 28, 33, 9, 17, 22, 24, 25, 26, 7]

loadTruck(truck1, payload1)
loadTruck(truck2, payload2)
loadTruck(truck3, payload3)

deliver_packages(truck1)
deliver_packages(truck2)
deliver_packages(truck3)

total_truck_miles = truck1.trip_total + truck2.trip_total + truck3.trip_total
total_elapsed_minutes = truck1.total_time_in_min + truck2.total_time_in_min + truck3.total_time_in_min

print(f"Total Trip Miles: {round(total_truck_miles, 2)}")
print(f"Total Trip Time: {math.floor(total_elapsed_minutes / Constant.MINUTES_PER_HOUR)} hour(s) {math.floor(total_elapsed_minutes % Constant.MINUTES_PER_HOUR)} minutes(s)")

main()
