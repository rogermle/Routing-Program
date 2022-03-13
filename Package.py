from HashTable import HashTable

import csv


class Package:
    def __init__(self):
        print("Display Package")
        self.package_hash_table = HashTable()

        # import data from CSV into HashTable
        with open('csv/packages.csv') as packages_file:
            csv_reader = csv.reader(packages_file, delimiter=',')
            for row in csv_reader:
                print(f'\t{row[0]} {row[1]} {row[2]}')
                self.package_hash_table.insert(row[0], row)

print("Package Loaded")
obj = Package()
print(obj.package_hash_table.table)
