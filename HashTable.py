# C950 - Webinar-1 - Let’s Go Hashing
# W-1_ChainingHashTable_zyBooks_Key-Value.py
# Ref: zyBooks: Figure 7.8.2: Hash table using chaining.
# Modified for Key:Value

# HashTable class using chaining.
import Constant
class HashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    # Time Complexity: O(N)
    # Space Complexity: O(N)

    def __init__(self, initial_capacity=40):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts package from CSV as a key value pair into the HashTable
    # Time Complexity: O(N)
    # Space Complexity: O(N)

    def insert(self, key, item):  # does both insert and update
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Search/Lookup for a package, returns package if successful
    # Pre Condition: Valid or Invalid Key as a parameter
    # Post Condition: Returns value if valid key, None if invalid key or not found
    # Time Complexity: O(N)
    # Space Complexity: O(N)

    def lookup(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        #print(bucket_list)

        # search for the key in the bucket list
        for kv in bucket_list:
            #print (kv)
            if kv[0] == key:
                return kv[1]  # value
        return None

    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])

    # Returns entire hashmap if successful
    # Pre Condition: None
    # Post Condition: Returns all values in Hash Table
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def all_table(self):
        return self.table

def loadPackageData():
    def loadPackageData():
        # import data from CSV into HashTable
        with open('csv/packages.csv') as packages_file:
            csv_reader = csv.reader(packages_file, delimiter=',')
            
            packageHashTable = HashTable()
            for data in csv_reader:
                id = data[Constant.ID]
                address = data[Constant.ADDRESS]
                city = data[Constant.CITY]
                state = data[Constant.STATE]
                zip_code = data[Constant.ZIP_CODE]
                due_datetime = data[Constant.DUE_DATETIME]
                weight = data[Constant.WEIGHT]
                notes = data[Constant.NOTES]
                status = Constant.AT_HUB_STATUS
                delivery_time = ''
                package = [id, address, city, state, zip_code, due_datetime, weight, notes,
                                                    status, delivery_time]
                
                #if 'Must be' in data[Constant.NOTES]:
                    #self.delivery1.append(package)
                #if 'EOD' != data[Constant.DUE_DATETIME] and 'NA' == data[Constant.NOTES]:
                    #self.delivery1.append(package)

                packageHashTable.insert(id, package)
        return packageHashTable

#Package Hashtable
packageHashtable = loadPackageData(packageFilename)