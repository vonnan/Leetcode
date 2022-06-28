# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        domain = startUrl.split("/")[2]
        q = deque([startUrl])
        visited = set([startUrl])
        res = [startUrl]
        
        while q:
            web = q.popleft()
            for url in htmlParser.getUrls(web):
                if url not in visited:
                    
                    visited.add(url)
                    if url.split("/")[2] == domain:
                        res.append(url)
                        q.append(url)
        
        return sorted(res)
        
        
        
        