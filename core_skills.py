import random
rand_list = [random.randint(1,20) for _ in range(10)]
print(rand_list)

list_comprehension_below_10 = []
for i in rand_list:
    if i < 10:
        list_comprehension_below_10.append(i)
print(list_comprehension_below_10)

def less_10(n):
    return n < 10

list_comprehension_below_10 = filter(less_10, rand_list)
print(list(list_comprehension_below_10))




#list_comprehension_below_10 =