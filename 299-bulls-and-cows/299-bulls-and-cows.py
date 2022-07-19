class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dic = {"A":0, "B": 0}
        counter_s, counter_g = Counter(secret), Counter(guess)    
        for s, g in zip(secret, guess):
            if s== g:
                dic["A"] += 1
                counter_s[s] -= 1
                counter_g[s] -= 1
        counter = counter_s & counter_g
        
        dic["B"] = sum(val for val in counter.values())
        
        return str(dic["A"]) + "A" + str(dic["B"]) + "B"
                
            