class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        points.sort()
        ls =[]
        dic = defaultdict(list)
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                if points[i][0]==points[j][0]:
                    if points[i][1]==points[j][1]:
                        dic[i].append("same")
                        dic[j].append("same")
                    else:    
                        dic[j].append("H")
                else:
                    dic[i].append(1000*(points[j][1]- points[i][1])/(points[j][0]-points[i][0]))
                    dic[j].append(1000*(points[j][1]- points[i][1])/(points[j][0]-points[i][0]))
        #print(dic)
        if len(points)==0:
            return 0
        res = 1
        for key, val in dic.items():
            temp = val.count("same")
            val = [v for v in val if v != "same"]
            if len(val) !=0:
                temp += max(Counter(val).values())
            temp += 1
            if res < temp:
                res = temp
        return res
 