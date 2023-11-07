
## The Problem
**[Eliminate Maximum Number of Monsters](https://leetcode.com/problems/eliminate-maximum-number-of-monsters/description/?envType=daily-question&envId=2023-11-07)**

This problem is of medium difficulty. But at first look, this might look a pretty ordinary problem. Well, it's not something extra-ordinary, but it do needs some practical thinking. And, it has the right to be a medium one (At least for me, I'm dumb anyway). However, this problem is really interesting. 

The problem states that, You are playing a video game where you are defending your city from a group of `n` monsters. Now, you have a weapon which you use to defeat monsters. You will be given two `lists`, one contains the `distances` of each monster from the city, and other the `speed` of the each monsters. Both lists are of same lenght, and `distance[i]` monster has the speeed of `speed[i]`. The speeds for each monster are constant. Now, the weapon you have has its' own drawbacks. It takes a minute to charge before it can fire again. The task is to determine, how many monsters you have defeated before your city gets attacked. If your city gets attacked before you could defeat all the monsters, you loose and return the number of monsters you defeated as your answer. You also lose, if the moment you charged and a distance of monster from the city is 0. That's it. That's the problem. 

But, there are some other things to note. 
* Initially, your weapon is fully charged, so, you kill the first monster without wasting your time. So, the counting down the time starts from the second monster.

## The Approach

The approach is pretty straight forward. 
* You calculate the `arrival time` for each monster with the constant velocity equation of motion, which is $ v = \frac{s}{t}$ and store them in a list. So, in this way the monster which is more faster should be the killed first, because the faster ones would close the distance quickly and will be closer than any other monsters.
* Then you sort the `arrival time` list in ascending order.
* Create a variable counter called `defeated` or `killed` or `time_counter` whichever you like and initialize with 0
* Now you iterate over the lenght of the `arrival time`
    * For each indx of `arrival time`.
        * `If` the `arrival time` <= `killed` or `defeated` or `time counter` (whichever you created), then break the loop. Because, it means the monster reached the city before the 1 minute time you could charge up your weapon.
        * `Else`, increase you `killed`, `defeated`, `time counter` by 1 and continue looping
* At last, `return` the counter variable as your answer

## The Code

```python
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:

        arrival_time = [] # creating the list to hold the arrival times of the monsters

        for distance, velocity in zip(dist, speed): 
            arrival_time.append(distance / velocity) # calculating the arrival times and storing them

        arrival_time.sort() # sorting the values from lowest to highest
        
        killed = 0 # creating the counter variable, initializing with zero

        for indx in range(len(arrival_time)): # the indx can be thought as the 1 minute interval time, so, every index is equivalent to 1 minutes have passed
            if arrival_time[indx] <= indx: # so for every minute, if the arrival time is less or equal, you lose, so break out of the loop and return the result
                break
            killed += 1 # else, increament the kill count
        
        return killed

```
