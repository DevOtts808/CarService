class Garage:
    def __init__(self, garageID, garageName, address, town, postCode, phoneNo):
        self.garageID = garageID
        self.garageName = garageName
        self.address = address
        self.town = town
        self.postCode = postCode
        self.phoneNo = phoneNo

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