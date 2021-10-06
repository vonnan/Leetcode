from bisect import bisect
class Solution:
    def nextClosestTime(self, time: str) -> str:
        hour, minute = time.split(":")
        sets = set(hour + minute)
        print(sets, hour, minute)
        hour_lst = sorted([a + b for a in sets for b in sets if a+b <="23"])
        min_lst = sorted([a + b for a in sets for b in sets if a+b <="59"])
        print(hour_lst, min_lst)
        idx_min = bisect(min_lst, minute)
        if idx_min != len(min_lst):
            return hour + ":" + min_lst[idx_min]
        else:
            if hour != hour_lst[-1]:
                idx = bisect(hour_lst, hour)
                return hour_lst[idx] + ":" + min_lst[0]
            else:
                return hour_lst[0] + ":" + min_lst[0]
        print(hour_lst, min_lst)