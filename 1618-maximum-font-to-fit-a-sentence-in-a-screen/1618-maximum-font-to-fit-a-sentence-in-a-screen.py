# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
#class FontInfo(object):
#    Return the width of char ch when fontSize is used.
#    def getWidth(self, fontSize, ch):
#        """
#        :type fontSize: int
#        :type ch: char
#        :rtype int
#        """
# 
#    def getHeight(self, fontSize):
#        """
#        :type fontSize: int
#        :rtype int
#        """
class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo : 'FontInfo') -> int:
        counter = Counter(text)
        print(counter, w, h)
        left, right = 0, len(fonts) -1
        font = fonts[left]
        if fontInfo.getHeight(font) > h or sum(fontInfo.getWidth(font, key)* val for key, val in counter.items()) > w:
            return -1
        
        while left < right:
            mid = (left + right + 1)//2
            font = fonts[mid]
            H = fontInfo.getHeight(font)
            if H  > h:
                right = mid -1
            else:
                tot = 0
                for key, val in counter.items():
                    width = fontInfo.getWidth(font, key)
                    tot += width * val
                    #print(width, key,val, tot)
                if tot > w:
                    right = mid -1
                else:
                    left = mid
        
        return fonts[left]
                