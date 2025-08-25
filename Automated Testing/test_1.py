def add(a,b):
    return a + b

#The prefix should be test(must start with test)
def test_add():
    #Telling what it should return
    assert add(2,3) == 5
    assert add(-1,-3) == -4

def test_add_big():
    assert add(200, 300) == 500
