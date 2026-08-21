class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # map position to index, then sort by position
        pos_index = {}
        for i in range(len(position)):
            pos_index[position[i]] = i
        position = sorted(position, reverse=True) 
        fleets = 0
        limiting_time = -1
        for i in range(len(position)):
            distance = target - position[i]
            curr_speed = speed[pos_index[position[i]]]
            arrival_time = distance / curr_speed
            if arrival_time > limiting_time:
                fleets += 1
                limiting_time = arrival_time
        return fleets
        