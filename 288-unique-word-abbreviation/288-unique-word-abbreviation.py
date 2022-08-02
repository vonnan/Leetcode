class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.dic = defaultdict(list)
        for word in dictionary:
            if len(word)<= 2:
                self.dic[word] = [word]
            else:
                self.dic[word[0] + str(len(word)-2) + word[-1]].append(word)
                

    def isUnique(self, word: str) -> bool:
        if len(word) <=2:
            return True
        
        abbrv = word[0] + str(len(word)-2) + word[-1]
        if abbrv not in self.dic or (self.dic[abbrv] == [word]):
            return True
        return False
    
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)