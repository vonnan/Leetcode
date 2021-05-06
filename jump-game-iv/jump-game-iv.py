from collections import defaultdict

class Solution:
    def minJumps(self, arr: List[int]) -> int:
	    n = len(arr)
	    validxs = defaultdict(list)
	    for i, a in enumerate(arr):
		    validxs[a].append(i)

	    queue = [0]
	    steps = 0
	    visited = set()
	    while queue:
		    next_queue = []
		    for pos in queue:
			    visited.add(pos)
			    if pos == n-1: return steps
			    if pos-1 not in visited and pos-1 >= 0: next_queue.append(pos-1)
			    if pos+1 not in visited and pos+1 < n: next_queue.append(pos+1)
			    next_queue.extend(validxs[arr[pos]])
			    del validxs[arr[pos]]

		    steps += 1
		    queue = next_queue

	    return steps          
        
        
                       
        
                
                
        
            
            
        
            
        