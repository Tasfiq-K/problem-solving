class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:

        arrival_time = []

        for distance, velocity in zip(dist, speed):
            arrival_time.append(distance / velocity)

        arrival_time.sort()
        
        killed = 0

        for indx in range(len(arrival_time)):
            if arrival_time[indx] <= indx:
                break
            killed += 1
        
        return killed
