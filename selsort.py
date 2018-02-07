import sys
list= [4,1,7,5,51,1,2,3]

for i in range(0,len(list)-1,1):
    print list
    for k in range(1,len(list)-1,1):
        if list[k]  > list[k+1]:
            temp = list[i]
            list[i] = list[k]
            list[k] = temp

print "Final"
print list
