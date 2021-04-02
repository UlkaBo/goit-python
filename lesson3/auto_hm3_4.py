def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price *= (1 - discount)
         

    apply_discount()
    return price
