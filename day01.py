# list_1 = [3,4,2,1,3,3]
# list_2 = [4,3,5,3,9,3]
input_file = 'input.txt'
values_1 = []
values_2 = []
deltas = []
d = 0
sum = 0

with open(input_file) as f:
    lines = f.readlines()

print(len(lines))

for i in lines:
    col_1, col_2 = i.split()
    values_1.append(col_1)
    values_2.append(col_2)

print(len(values_1))

values_1.sort()
values_2.sort()

# Assuming lists are same size; prob not a good idea
for i in range(0,len(values_1)):
    if int(values_1[i]) < int(values_2[i]):
        # print(values_2[i] - values_1[i])
        d = int(values_2[i]) - int(values_1[i])
        print(d)
    else:
        # print(values_1[i] - values_2[i])
        d = int(values_1[i]) - int(values_2[i])
        print(d)
    deltas.append(d)

# Add up the deltas
for i in deltas:
    sum+=i

print(sum)
exit()
