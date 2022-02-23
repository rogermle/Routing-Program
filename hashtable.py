# C950 - Webinar-1 - Let’s Go Hashing
# W-1_ChainingHashTable_zyBooks_Key-Value.py
# Ref: zyBooks: Figure 7.8.2: Hash table using chaining.
# Modified for Key:Value

# HashTable class using chaining.
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
        # print(bucket_list)

        # search for the key in the bucket list
        for kv in bucket_list:
            # print (key_value)
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


bestMovies = [
    [1, "CITIZEN KANE - 1941"],
    [2, "CASABLANCA - 1942"],
    [3, "THE GODFATHER - 1972"],
    [4, "GONE WITH THE WIND - 1939"],
    [5, "LAWRENCE OF ARABIA - 1962"],
    [6, "THE WIZARD OF OZ - 1939"],
    [7, "THE GRADUATE - 1967"],
    [8, "ON THE WATERFRONT- 1954"],
    [9, "SCHINDLER'S LIST -1993"],
    [10, "SINGIN' IN THE RAIN - 1952"],
    [11, "STAR WARS - 1977"]
]

myHash = HashTable()

print("\nInsert:")
myHash.insert(bestMovies[0][0], bestMovies[0][1])  # 2nd bucket; Key=1, item="CITIZEN KANE - 1941"
print(myHash.table)

myHash.insert(bestMovies[10][0], bestMovies[10][1])  # 2nd bucket as well; Key=11, item="STAR WARS - 1977"
print(myHash.table)

print("\nSearch:")
print(myHash.lookup(1))  # Key=1, item="CITIZEN KANE - 1941"
print(myHash.lookup(11))  # Key=11, item="STAR WARS - 1977"; so same bucket and Chainin is working

print("\nUpdate:")
myHash.insert(1, "Star Trek - 1979")  # 2nd bucket; Key=1, item="Star Trek - 1979"
print(myHash.table)

print("\nRemove:")
myHash.remove(1)  # Key=1, item="Star Trek - 1979" to remove
print(myHash.table)

myHash.remove(11)  # Key=11, item="STAR WARS - 1977" to remove
print(myHash.table)

