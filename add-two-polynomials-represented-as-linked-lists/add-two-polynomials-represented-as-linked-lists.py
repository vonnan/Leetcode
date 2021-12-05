# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        dummy = PolyNode(0, 0, None)
        node = dummy
        
        while poly1 and poly2:
            #print(poly1.power, poly2.power, node.power, node.coefficient)
            if poly1.power == poly2.power:
                x = poly1.coefficient + poly2.coefficient
                
                if x != 0:
                    node.next = PolyNode(x, poly1.power, None)
                    node = node.next
                
                poly1 = poly1.next
                poly2 = poly2.next
                    
            elif poly1.power > poly2.power:
                node.next = PolyNode(poly1.coefficient, poly1.power, None)
                poly1 = poly1.next
                node = node.next
            else: 
                node.next = node.next = PolyNode(poly2.coefficient, poly2.power, None)
                poly2 = poly2.next
                node = node.next
            
        if not node:
            return dummy.next
       
        
        poly = poly1 or poly2
        if poly:
            node.next = poly
        return dummy.next
        
        
                    