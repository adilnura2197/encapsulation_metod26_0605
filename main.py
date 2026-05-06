class Transport:
    def __init__(self, passengers, capacity):
        self._passengers = passengers
        self._capacity = capacity


class Bus(Transport):
    def add_passenger(self, n):
        self._passengers += n
        print(f"Passengers:{self._passengers}")

    def remove_passenger(self, n):
        self._passengers -= n
        print(f"Passengers:{self._passengers}")

    def info(self):
        print(f"Passengers:{self._passengers}")


b1 = Bus(20, 50)

b1.add_passenger(1)
b1.remove_passenger(3)
