class Solution:
    def maskPII(self, s: str) -> str:
        flag = False
        if "@" in s:
            lst = s.split("@")
            flag = True
        if flag:
            lst[0] = lst[0][0].lower()+ "*****" + lst[0][-1].lower()
            lst[1] = lst[1].lower()
            return "@".join(lst)
        
        phone = [ch for ch in s if ch.isdigit()]
        
        if len(phone) == 10:
            return "***-***-" + "".join(phone[-4:])
        
        else:
            return "+" +"*"*(len(phone) - 10) + "-***-***-" + "".join(phone[-4:])
        
        
            
        
        