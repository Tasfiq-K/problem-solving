class MyCalendarTwo:
    def __init__(self):
        self.single_bookings = []
        self.double_bookings = []

    def book(self, start: int, end: int) -> bool:
        for double_start, double_end in self.double_bookings:
            if start < double_end and end > double_start:
                return False
            
        for single_start, single_end in self.single_bookings:
            if start < single_end and end > single_end:
                self.double_bookings.append((max(start, single_start), min(end, single_end)))
        
        self.single_bookings.append((start, end))
        return True