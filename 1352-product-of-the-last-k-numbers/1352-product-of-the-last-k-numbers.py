class ProductOfNumbers:

    def __init__(self):
        self.q = []
        self.product = [1]
        
    def add(self, num: int) -> None:
        self.q.append(num)
        self.product.append(self.product[- 1] * num)

    def getProduct(self, k: int) -> int:
        res = 1
        
        if self.product[ - (k+1)] != 0:
            return self.product[-1]//self.product[-(k+1)]
        elif 0 in self.q[-k:]:
            return 0
        else:
            for num in self.q[-k:]:
                res *= num
            return res
            
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)