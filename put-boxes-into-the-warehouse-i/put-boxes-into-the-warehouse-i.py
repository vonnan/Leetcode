class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        for i in range(1,len(warehouse)):
            warehouse[i] = min(warehouse[i], warehouse[i-1])
            
        boxes.sort()
        
        count = 0
        
        if boxes[0] > warehouse[0]:
            return count
        
        for box in boxes:
            while warehouse and warehouse[-1] < box:
                warehouse.pop()
            if not warehouse:
                return count
            else:
                warehouse.pop()
                count += 1
            
        return count
                
                
            