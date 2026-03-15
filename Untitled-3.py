files_names = ['document1.txt', 'image1.jpg', 'document2.txt', 'image2.jpg']

for file_name in files_names:
    print(file_name)
    
greeting = 'Hello, world!'

count_o = 0
for char in greeting:
    if char == 'o':
        count_o += 1
print(count_o)

range_objects = range(10)
print(range_objects)

numbers = list(range_objects)
print(numbers)

num = [10,11,12,13]

for i in range(len(num)):
    print(i)
    num[i] += 1
print(num)

num_1 = [1,2,3,4,5]
num_2 = [1,2,3,4,5,6,7,8]

average_1 = sum(num_1) / len(num_1)
print(average_1)

def find_average(numbers):
    average = sum(numbers) / len(numbers)
    return average
average_1 = find_average(num_1)
average_2 = find_average(num_2)
print(average_1)
print(average_2)

def format_date(day: int, month: str) -> str:
    return f"The date is {day} of {month}"

print(format_date(15,"March"))

def my_func():
    local_var = "I'm local variable"
    print(local_var)
my_func()
print(local_var)