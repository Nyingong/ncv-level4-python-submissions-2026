#Classproduct examples
class Product:
    VAT_RATE=0.15
    
    def _init_(self, code, name, price):
        self.code=code
        self.name=name
        
        if price <0:
            raise ValueError("Price cannot be negative.")
        
        self.price=price
    
    def _str_(self):
        return f"{self.code}-{self.name}: R{self.price:.2f}"
    
    def calc_vat(self):
        return self.price*self.VAT_RATE
    
    def price_including_vat(self):
        return self.price+self.calc_vat()
    
    def apply_discount(self, percentage):
        discount=self.price*percentage/100
        return self.price-discount
    
    def main():
        product1=product("P001", "Keyboard", 450.00)
        PRODUCT2=product("P002", "Mouse", 250.00)
        
        print(product1)
        print(product2)
        
        print("VAT:", product1.calc_vat())
        print("Price including VAT:", product1.price_including_vat())
        print("Price after 10% discount:", product1.appy_discount(10))
        
    main()
    
    
    
    