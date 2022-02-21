class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        value = 0
        
        for amount_of_boxes, units in boxTypes:
            if truckSize > 0:
                amount_to_take = min(truckSize, amount_of_boxes)
                value += (amount_to_take * units)
                truckSize -= amount_to_take
            else:
                return value
            
        return value