# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

# Input
# ["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
# [[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]

# Output
# [null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]

# Explanation
# UndergroundSystem undergroundSystem = new UndergroundSystem();
# undergroundSystem.checkIn(45, "Leyton", 3);
# undergroundSystem.checkIn(32, "Paradise", 8);
# undergroundSystem.checkIn(27, "Leyton", 10);
# undergroundSystem.checkOut(45, "Waterloo", 15);  // Customer 45 "Leyton" -> "Waterloo" in 15-3 = 12
# undergroundSystem.checkOut(27, "Waterloo", 20);  // Customer 27 "Leyton" -> "Waterloo" in 20-10 = 10
# undergroundSystem.checkOut(32, "Cambridge", 22); // Customer 32 "Paradise" -> "Cambridge" in 22-8 = 14
# undergroundSystem.getAverageTime("Paradise", "Cambridge"); // return 14.00000. One trip "Paradise" -> "Cambridge", (14) / 1 = 14
# undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 11.00000. Two trips "Leyton" -> "Waterloo", (10 + 12) / 2 = 11
# undergroundSystem.checkIn(10, "Leyton", 24);
# undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 11.00000
# undergroundSystem.checkOut(10, "Waterloo", 38);  // Customer 10 "Leyton" -> "Waterloo" in 38-24 = 14
# undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 12.00000. Three trips "Leyton" -> "Waterloo", (10 + 12 + 14) / 3 = 12

class UndergroundSystem:

    def __init__(self):
        self.start_stations = {}
        self.end_stations = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin_id = id
        # self.start_stations = {}
        self.init_time = t

        if stationName not in self.start_stations:
            self.start_stations[stationName] = []
            self.start_stations[stationName].append(self.init_time)
        else:
            self.start_stations[stationName].append(self.init_time)

        print(f"start stations: {self.start_stations}")
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.checkout_id = id
        # self.end_stations = {}
        self.end_time = t

        if not stationName in self.end_stations:
            self.end_stations[stationName] = []
            self.end_stations[stationName].append(self.end_time)
        else:
            self.end_stations[stationName].append(self.end_time)
        print(f"end stations: {self.end_stations}")

        # if self.checkin_id == self.checkout_id:
        #     self.travel_time = self.end_time - self.init_time
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        print(f"start station Name {self.start_stations}. end stattions {self.end_stations}")
        sum = 0
        if len(self.start_stations[startStation]) == len(self.end_stations[endStation]):
            for i in range(len(self.start_stations[startStation])):
                sum += (self.end_stations[endStation][i] - self.start_stations[startStation][i])
            avg = (sum / len(self.start_stations[startStation]))
        elif len(self.start_stations[startStation]) < len(self.end_stations[endStation]):
            for i in range(len(self.start_stations[startStation])):
                sum += (self.end_stations[endStation][i] - self.start_stations[startStation][i])
            avg = (sum / len(self.start_stations[startStation]))
        else:
            for i in range(len(self.end_stations[endStation])):
                sum += (self.end_stations[endStation][i] - self.start_stations[startStation][i])
            avg = (sum / len(self.end_stations[endStation]))

        return avg


# undergroundSystem = UndergroundSystem()
# undergroundSystem.checkIn(45, "Leyton", 3)
# undergroundSystem.checkIn(32, "Paradise", 8)
# undergroundSystem.checkIn(27, "Leyton", 10)
# undergroundSystem.checkOut(45, "Waterloo", 15)
# undergroundSystem.checkOut(27, "Waterloo", 20)
# undergroundSystem.checkOut(32, "Cambridge", 22)
# print(undergroundSystem.getAverageTime("Paradise", "Cambridge"))
# print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))
# undergroundSystem.checkIn(10, "Leyton", 24)
# print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))
# undergroundSystem.checkOut(10, "Waterloo", 38)
# print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))

ugsystem = UndergroundSystem()
ugsystem.checkIn(10, "Leyton", 3)
ugsystem.checkOut(10, "Paradise", 8)
print(ugsystem.getAverageTime("Leyton", "Paradise"))
ugsystem.checkIn(5, "Leyton", 10)
ugsystem.checkOut(5, "Paradise", 16)
print(ugsystem.getAverageTime("Leyton", "Paradise"))
ugsystem.checkIn(2, "Leyton", 21)
ugsystem.checkOut(2, "Paradise", 30)
print(ugsystem.getAverageTime("Leyton", "Paradise"))

# a_dict = {}
# a_key = 'k'
# if a_key not in a_dict:
#     a_dict[a_key] = []
# print(a_dict)
# a_dict['k'].append(5)
# print(a_dict)
# a_dict['k'].append(6)
# print(a_dict)

# a_dict = {'a': [2, 3, 4],
#           'b': [1, 2, 3]}

# for i in range(len(a_dict['a'])):

#     print(a_dict['a'][i] - a_dict['b'][i])