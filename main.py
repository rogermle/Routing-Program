# Roger Le
# C950 Performance Assessment
# Student ID: 1060770

import Package
from Truck import Truck
import csv
from datetime import datetime


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
   
      
main()