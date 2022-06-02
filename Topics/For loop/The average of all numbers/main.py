# put your python code here
a = int(input())
b = int(input())
my_sum = count = 0
my_list = []
for i in range(a, b + 1):
    if i % 3 == 0:
        #calculate mean of all numbers
        my_sum = my_sum + i
        count = count + 1
        my_list.append(i)

print(my_sum / count)

from statistics import mean
print(mean(my_list))

print((sum(my_list) / len(my_list)))

