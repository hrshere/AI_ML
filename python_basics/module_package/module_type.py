'''modules can have submodules,variables or fn values'''
import numpy
print("numpy.random is a", type(numpy.random))
print("it contains names such as...",
      dir(numpy.random)[-15:])

#roll 10 dice
rolls = numpy.random.randint(low=1,high=6,size=10)
print(rolls)
print(type(rolls))
print(rolls.mean())
print(rolls.tolist())
print(rolls.ravel())
print(rolls + 10)
print(rolls>=3)

xlist = [[1,2,3],[2,4,6]]
x = numpy.asarray(xlist)
print("xlist = {}\nx =n{}".format(xlist, x))
print(x[1,-1])