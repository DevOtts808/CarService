class Garage:
    def __init__(self, garageID, garageName, address, town, postCode, phoneNo):
        self.garageID = garageID
        self.garageName = garageName
        self.address = address
        self.town = town
        self.postCode = postCode
        self.phoneNo = phoneNo


def addGarage():
    namesOfGarages = []
    garageID = input("Input garage id:")
    garageName = input("Input garage name:")
    address = input("Input garage address:")
    town = input("Input garage town:")
    postCode = input("Input garage postcode:")
    phoneNo = input("Input garage phone number:")

    garageOne = Garage(garageID, garageName, address, town, postCode, phoneNo)
    namesOfGarages.append(garageOne.__dict__)
    print(namesOfGarages)

    garageID = input("Input garage id:")
    garageName = input("Input garage name:")
    address = input("Input garage address:")
    town = input("Input garage town:")
    postCode = input("Input garage postcode:")
    phoneNo = input("Input garage phone number:")

    garageTwo = Garage(garageID, garageName, address, town, postCode, phoneNo)
    namesOfGarages.append(garageTwo.__dict__)
    databaseNum = input("what databse number")

    print(namesOfGarages[databaseNum])


addGarage()


class Job:
    def __init__(self, jobID, carRegNo, garageID, datein, dateout, cost):
        self.jobID = jobID
        self.carRegNo = carRegNo
        self.garageID = garageID
        self.datein = datein
        self.dateout = dateout
        self.cost = cost


class Customer:
    def __init__(self, customerID, forename, surname, address, postcode, phoneNo):
        self.customerID = customerID
        self.forename = forename
        self.surname = surname
        self.address = address
        self.postcode = postcode
        self.phoneNo = phoneNo


class Car:
    def __init__(self, regNo, make, model, year, customerID):
        self.regNo = regNo
        self.make = make
        self.model = model
        self.year = year
        self.customerID = customerID