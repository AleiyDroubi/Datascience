a=12
p=6
def foo(a):
    a=cat(a+1)
    print("in foo",a,"and",p)
def bar(i):
    i=i+2
    print("in bar ",i)
def cat(a):
    a=a+10
    bar(a)
    print("in cat ",a)
    return a
foo(a)