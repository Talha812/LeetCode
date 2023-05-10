class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        boxTypes.sort(key = lambda x : x[1], reverse = True)

        units = 0

        for box in boxTypes:
            no_of_boxes = box[0]
            unit_per_box = box[1]

            if no_of_boxes <= truckSize:
                units += (no_of_boxes * unit_per_box)
                truckSize -= no_of_boxes
            
            else:
                units += (truckSize * unit_per_box)
                truckSize = 0
                break
        
        return units

