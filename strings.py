"""
numbers=[10,11,12,13]
for b in numbers:
    print("hello besteee")
    """

urunler = []
adet = int(input("kaç ürün eklemek istıyorsunuz? "))
i=0

while i < adet :
    name = input("ürün adı=")
    price = input("fiyatı ne kadar?")
    urunler.append ({
        "name": name,
        'price': price
         })
    i+=1
for urun in urunler: 
    print(f'ürün adı: {urun ["name"]} ve ürün fiyatı: {urun ["price"]}')



 
 
