## The Problem
**[Seat Reservation Manager](https://leetcode.com/problems/seat-reservation-manager/description/?envType=daily-question&envId=2023-11-06)**

It's a seat reserving types of of problem. Where you need to design a system, that can reserve empty seats, can unreserve any reserved seats and let it available for future reservation. The main goal of the problem is, you need to keep track of the unreserved seats, so that when the reservation is made in the future, the smallest seat number get reserved first out of the unreserved seats. 

## The Approach

There are a lot of ways that can be taken to solve this problem. The approach that I've taken is good on memory consumption but slow on memory. Takes about 641 ms, which is almost 1.5 times of most of the solutions. However, It's still the approach that I thought at first. So, first let's go over it.

* First, we create two instance variables. One is to hold the currently booked seat's number (initialize with 0), let's call it `seats` and other is to hold the unreserved seat's number. Let's call it `temp`
* Next, we create the `reserve` method. We first check ->
    * `If` there are any unreserved seats, if not we increase the `seats` to 1 and return it. Which means that the seat 1 is now booked.
    * `Else`, if there are unreserved seats, then we simply take the smallest number from the list and return it. We take the smallest number, because the smallest numbered seats should be booked first. The seats get booked in ascending order.
* Then, we create the `unreserve` method. This method takes the `seat_number` as an argument. 
    * First, we check if the passed `seat_number` is equal to the number of the last booked seat.
        * `If` it is then we simply subtract 1 from the `seats`. Because, if we reserve any seat next time and if we don't have any smallest seat number in our `temp` list, then the `seats` will be increased to the number that we subtracted from. 
        * `Else`, we add the `seat_number` to the `temp` list and `sort` it in ascending order. 

That's it.

## The Code

### My Approach

```python
class SeatManager:
    
    def __init__(self, n: int):
        self.reservations = n # well, this doesn't get used! created anyway, thought of using. Uh! well! 
        self.seats = 0 # current seat number holder
        self.temp = [] # unreserved seats number holder

    def reserve(self) -> int:
        if not self.temp: # check if temp is empty or not
            self.seats += 1 # increase seats by 1 if the temp is empty, and return it
            return self.seats 

        return self.temp.pop(0) # if temp not empty, return the 1st item from the temp list, which will be the smallest number of the list.

    def unreserve(self, seatNumber: int) -> None:
        if seatNumber == self.seats: # check if the seat_number to unreserve is equal to the current seat number
            self.seats -= 1 # if True, then decrease the current seat number by 1
        else:
            self.temp.append(seatNumber) # append the seat_number to the temp list
            self.temp = sorted(self.temp) # sort the list in ascending order, so that when we pop the first item, it will be the smallest
```

### Optimal Approach

**Will add later, too lazy to do now** 🥱