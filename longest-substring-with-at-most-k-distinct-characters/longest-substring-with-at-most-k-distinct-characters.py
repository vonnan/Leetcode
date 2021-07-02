class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        counter = Counter()
        left, count, res =0, 0, 0
        seen = set()
        
        for right, ss in enumerate(s):
            if ss not in seen:
                count += 1
                seen.add(ss)
                
            counter[ss] += 1
            
            while count > k:
                if counter[s[left]] ==1:
                    count -= 1
                    seen.remove(s[left])
                counter[s[left]] -= 1
                left += 1
                
            res = max(res, right - left + 1)
            
        return res
                
            
                    