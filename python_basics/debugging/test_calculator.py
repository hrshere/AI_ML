'''in terminal window type pytest test_calculator.py -> F(something failed) E(hints about error)'''
from calculator import square




def test_posetive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0
        
