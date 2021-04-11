def is_valid_pin_codes(pin_codes):
    if len(pin_codes) != len(set(pin_codes)) :
        return False
        
    for pin in pin_codes:
        if type(pin) != str : 
            return False
        if len(pin) != 4 :    
            return False
        if not(pin.isdigit()) :    
            return False
    return bool(pin_codes)
n = []
print(is_valid_pin_codes(n))

