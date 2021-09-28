class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        bits = bits[:-1]
        while bits:
            if bits[0] == 0:
                bits.pop(0)
            elif len(bits) >=2:
                bits.pop(0)
                bits.pop(0)
            else:
                break
        return len(bits) == 0