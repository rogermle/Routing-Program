import csv
#import data
import datetime

#Reads the csv files(desinations) and creates a dictionary from raw data to unique IDs for usage on the algorithm below.
distanceData = 'csv/distances.csv'
addressData = 'csv/addresses.csv'
distance_dict = {}
address_dict = {}

def loadAddressData(addressData):
    with open(addressData) as addressCSV:
        addresses = list(csv.reader(addressCSV, delimiter=','))
        for address in addresses:
            address_dict[address[2].strip()] = address[0]
    
    #print(address_dict)
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
    #print(distance_dict)

# Time Complexity O(1)
# Space Complexity O(N)
def distanceBetween(fromAddress, toAddress):

    try:
        distance = distance_dict[f'{address_dict[fromAddress]}{address_dict[toAddress]}']
        if distance == '':
            distance = distance_dict[address_dict.index(toAddress)][address_dict.index(fromAddress)]
    except:
        print("Error Condition")

    return distance


loadAddressData(addressData)
loadDistanceData(distanceData)
print(distanceBetween('1060 Dalton Ave S','3595 Main St')) # Returns 6.0 as expected