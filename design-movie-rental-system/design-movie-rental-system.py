from sortedcontainers import SortedList
class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.dic = defaultdict(SortedList)
        self.shop = defaultdict(set)
        self.price = defaultdict(list)
        self.rented = SortedList()
        for shop, movie, price in entries:
            self.dic[movie].add((price, shop))
            self.shop[shop].add(movie)
            self.price[(shop, movie)] = price
        
    def search(self, movie: int) -> List[int]:
        return [shop for _, shop in self.dic[movie][:5]]
        
    def rent(self, shop: int, movie: int) -> None:
        if movie in self.shop[shop]:
            p = self.price[(shop, movie)]
            self.rented.add((p, shop, movie))
            self.dic[movie].remove((p, shop))
            self.shop[shop].add(movie)
      
    def drop(self, shop: int, movie: int) -> None:
        p = self.price[(shop, movie)]
        self.dic[movie].add((p, shop))
        self.rented.remove((p, shop, movie))
        self.shop[shop].add(movie)
        
    def report(self) -> List[List[int]]:
        return [(s,m) for _,s,m in self.rented[:5]]
    
            
        
        


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()