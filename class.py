class Items:
    def __init__ (self,id: str,name: str,price: int,purchase_price: int):
        self.id = id
        self.name = name
        self.price = price
        self.purchase_price = purchase_price
    def cost_rate (self):
        return self.purchase_price / self.price
    
item1 = Items("A0001","半袖クールシャツ",6000,2250)
print(item1.cost_rate())