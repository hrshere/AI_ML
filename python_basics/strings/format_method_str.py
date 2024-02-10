'''formats specified values and insert them in string placeholder'''
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 46))

txt1 = "My name is {}, I'm {}".format("Himanshu", 55)
print(txt1)

txt2 = "My name is {0}, I'm {1},call me {0}".format("John", 33)
print(txt2)

txt3 = "My name is {fname}, I'm {age}".format(fname = "John",age="21")
print(txt3)
planet = "Pluto"
pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
stmt = "{} weighs about {:.2} Kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(planet, pluto_mass,pluto_mass/earth_mass,population)
print(stmt)