def is_negative(number):
    return number<0

def exactly_one_topping(Ketchup=0, mustard=0, onion=0) :
    '''Return whether the customer wants exactly one of the three available toppings on their hot dog'''
    # return int(Ketchup)+int(mustard)+int(onion)==1
    return (Ketchup+mustard+onion) == 1

print(exactly_one_topping(1))