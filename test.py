class Hunter():
   def __init__(self,net_worth):
      self.net_worth = net_worth

   def bitcoin(self):
      bitcoin_value = self.net_worth/66000
      return bitcoin_value
   
hunter = Hunter(758481).bitcoin()
print(hunter)
      

list = [ "banana","good",
        "apple","mid"]

print(5 == 6)

array = 1,2,3
print(array[1])
with open("genius.jpg" , "r") as F:
   file = list(F)
