# write your own program to demonstrate the concept of inheritance in python
class products:
     def __init__(self, name, price):
         self.name = name
         self.price = price

     def buy(self):
         print("the product is available")

product1 = products("tissue",12 )
print(product1.name)
print(product1.buy())
