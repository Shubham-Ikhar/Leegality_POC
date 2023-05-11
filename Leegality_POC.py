class ParkingLot:
    def __init__(self):
        self.levelA = Level("A")
        self.levelB = Level("B")

    def assign_spot(self, vehicle_number):
        for spot in self.levelA.spots:
            # import pdb;pdb.set_trace()
            if spot.is_empty():
                spot.assign(vehicle_number)
                return {"level": "A", "spot": spot.number}
        for spot in self.levelB.spots:
            if spot.is_empty():
                spot.assign(vehicle_number)
                print("done")
                return {"level": "B", "spot": spot.number}
        return None

    def retrieve_spot(self, vehicle_number):
        for spot in self.levelA.spots:
            if spot.vehicle_number == vehicle_number:
                return {"level": "A", "spot": spot.number}
        for spot in self.levelB.spots:
            if spot.vehicle_number == vehicle_number:
                return {"level": "B", "spot": spot.number}
        return None


class Level:
    def __init__(self, name):
        self.name = name
        self.spots = [Spot(i + 1) for i in range(20)]


class Spot:
    def __init__(self, number):
        self.number = number
        self.vehicle_number = None

    def is_empty(self):
        return self.vehicle_number is None

    def assign(self, vehicle_number):
        self.vehicle_number = vehicle_number

obj = ParkingLot()
print(obj.assign_spot(4503))

