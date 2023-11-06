class SeatManager:
    
    def __init__(self, n: int):
        self.reservations = n
        self.seats = 0
        self.temp = []

    def reserve(self) -> int:
        if not self.temp:
            self.seats += 1
            return self.seats
        print(self.temp)

        return self.temp.pop(0)

    def unreserve(self, seatNumber: int) -> None:
        if seatNumber == self.seats:
            self.seats -= 1
        else:
            self.temp.append(seatNumber)
            self.temp = sorted(self.temp)