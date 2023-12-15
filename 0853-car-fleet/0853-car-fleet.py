class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        # stack = []

        # for p, s in fleets:
        #     stack.append((target - p)/ s) 
        #     if len(stack) >= 2 and stack[-1] <= stack[-2]:
        #         stack.pop()

        # return len(stack)
  
        last_arrival_time = float('-inf')
        count = 0

        for p, s in fleets:
            arrival_time = (target - p) / s

            if arrival_time > last_arrival_time:
                count += 1
                last_arrival_time = arrival_time

        return count
 