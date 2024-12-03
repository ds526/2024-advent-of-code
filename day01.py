list_1 = [3,4,2,1,3,3]
list_2 = [4,3,5,3,9,3]

list_1.sort()
list_2.sort()
deltas = []
d = 0
sum = 0

for i in range(0,len(list_1)):
    if list_1[i] < list_2[i]:
        print(list_2[i] - list_1[i])
        d = list_2[i] - list_1[i]
    else:
        print(list_1[i] - list_2[i])
        d = list_1[i] - list_2[i]
    deltas.append(d)

print("======")

for i in deltas:
    sum+=i

print(sum)
