def calculate_discount(price,discount_percentage):
    

    if discount_percentage > 20 :
        new_price=price-(10/100*price)
        print(new_price)

    else:
        print(price)

calculate_discount(10000,30)
    

