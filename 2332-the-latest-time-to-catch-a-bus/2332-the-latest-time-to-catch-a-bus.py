class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        
        passenger = 0
        for bus in buses:
            bussFilled = False
            curr_cap = 0
            
            while passenger < len(passengers) and passengers[passenger] <= bus and curr_cap != capacity:
                passenger += 1
                curr_cap += 1
                
            if curr_cap == capacity:
                bussFilled = True
                
        if bussFilled:
            max_seat = passengers[passenger - 1]
        else:
            max_seat = buses[-1]
    
        bookedSeats = passengers
        for seat in range(max_seat, 0, -1):
            if seat not in bookedSeats:
                return seat
            