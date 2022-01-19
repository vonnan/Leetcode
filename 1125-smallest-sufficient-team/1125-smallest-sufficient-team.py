class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        dic = {val:i for i, val in enumerate(req_skills)}
        n = len(dic)
        
        masks = []
        dp = defaultdict(list)
        dp[0] = []
        for i, p in enumerate(people):
            p_skill = 0
            for val in p:
                p_skill |= 1 <<dic[val]
            #for skillset, need in list(dp.items()):
            for skillset, need in (dp.items()):
                with_p = p_skill | skillset
                if skillset == with_p:
                    continue
                if with_p not in dp or len(dp[with_p]) > len(need) + 1:
                    dp[with_p] = need + [i]
        return dp[(1<<n) -1]
            
        
                
            