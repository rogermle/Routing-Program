from HashTable import HashTable

import csv


class Package:
    def __init__(self):
        print("Display Package")
        self.package_hash_table = HashTable()

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
                delivery_start_time = ''

                self.package_hash_table.insert(id, [id, address, city, state, zip_code, due_datetime, weight, notes,
                                                    status, delivery_start_time])
print("Package Loaded")
obj = Package()
# print(obj.package_hash_table.table)

print(obj.package_hash_table.lookup('38'))
