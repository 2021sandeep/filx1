def f1():
    yield 1
    yield 2
    yield 3
result=f1()
for value in result:
    print(value)
#######################
def f2():
    for i in range(10):
        yield i
result=f2()
for value in result:
    print(value)
###########################
def f2():
    for i in range(10):
        yield i
result=f2()
print(result.__next__())
print(result.__next__())
print(result.__next__())
print(result.__next__())
