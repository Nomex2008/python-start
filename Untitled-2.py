#lesson 4
my_list_fruits = ['apple', 'banana', 'cherry', True]
my_list_fruits2 = ['apple', 'banana', 'cherry', False]
print(my_list_fruits)
print(len(my_list_fruits))
print(my_list_fruits == my_list_fruits2)
print('apple' in my_list_fruits)

my_list_fruits3 = my_list_fruits + my_list_fruits2
print(my_list_fruits3)
my_list_fruits3.append('watermelon')
print(my_list_fruits3)
watermelon = my_list_fruits3.pop()
print(watermelon)
print(my_list_fruits3)
my_list_fruits3_reverse = my_list_fruits3
my_list_fruits3_reverse.reverse()
print(my_list_fruits3_reverse)

numbers_list = [1,5,3]
numbers_list.sort()
print(numbers_list)
numbers_list.sort(reverse=True)
print(numbers_list)
print(max(numbers_list))
print(min(numbers_list))
print(sum(numbers_list))