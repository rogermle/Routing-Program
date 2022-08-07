



# Used to encapsulate the Package object

# Working with raw values is not preferred experience
class Package:
    def __init__(self, id, address, city, state, zip_code, due_datetime, weight, notes):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.due_datetime = due_datetime
        self.weight = weight
        self.notes = notes
        self.status = "AT HUB"
        self.delivery_time = ''
