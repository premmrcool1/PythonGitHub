import sys
list1 = []
def enque(x):
    list1.append(x)

def deque():
    k=len(list1)
    list1.remove(list1[k-1])


enque(4)
enque(5)
enque(6)
enque(6)
enque(61)
enque(89)

deque()
print list1