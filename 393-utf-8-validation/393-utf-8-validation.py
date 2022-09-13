class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        data = [bin(d)[2:].zfill(8) for d in data]
        
        while data:
            d = data.pop(0)
            if d[0] == "0":
                continue
            else:
                for j in range(1, 8):
                    if d[j] == "0":
                        break
                
                j -= 1
                if j < 1 or j > 3:
                    return False
                if len(data) < j:
                    return False
                while j:
                    if data.pop(0)[:2] != "10":
                        return False
                    j -= 1
        return True