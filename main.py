# Roger Le
# C950 Performance Assessment
# Student ID: 1060770

from Package import Package
from Truck import Truck
import csv
from datetime import datetime
from HashTable import HashTable

packageHashTable = HashTable()


truck1 = Truck('08:05')
truck2 = Truck('09:15')
truck3 = Truck('10:20')

#payload1 = [17, 21]

#truck1.load(self, payload1)


def main():
   print("Welcome to WGU Package Delivery")
   print("\r\n")
   print("Please select one of the following options:")
   print("\r\n")
   print("Package Look up by ID Press 1")
   print("All Packages by Time in HH:MM format Press 2")
   print("Exit Application Press 3")
   
   choice = input("Please enter a valid number: ")

   if (choice == "1"):
      print("Package Lookup")
      id = input("Please enter a valid package ID (1-40): ")
      pretty_print_package(id)
   elif (choice == "2"):
      print("Date Time Lookup")
      time = input("Please enter a time after 08:00:00 to search package statuses (in military time e.g 0900): ")
      # Truck.delivery_time = datetime.combine(datetime.today().day(), datetime.strptime(time, "%H:%M").time())
      
      print(time)
   elif (choice == "3"):
      exit()
   else:
      main()
   

def pretty_print_package(id):
   package = Package.obj.package_hash_table.lookup(id)
   print(f' ID: {package[0]} | Address: {package[1]} | City: {package[2]} | Zip: {package[4]} | Due Date: {package[5]} | Weight: {package[6]} | Status: {package[8]}')
   
   
def print_all_packages(time):
   print("Packages at {time}: \r\n")


def loadPackages():
   print("Display Package")
   global packageHashTable

        # import data from CSV into HashTable
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
   #print(obj.package_hash_table.table)

   #print(obj.package_hash_table.lookup('33'))
   
loadPackages()
print(packageHashTable.lookup(15))
main()
