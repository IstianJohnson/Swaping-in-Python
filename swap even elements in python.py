#program to swap elements at even index number

l = [0,1,2,3,4,5,6,7]
l1 = l[0::2]
l2 = l[1::2]

l3 = l1[0::2]
l4 = l1[1::2]

l5 = []
for i in range(len(l3)):
    l5.append(l4[i])
    l5.append(l3[i])

l6 = []
for a in range(len(l2)):
    l6.append(l5[a])
    l6.append(l2[a])
    
print(l6)
