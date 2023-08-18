#List comprenhension

numbers = [1,1,2,3,5,8,13,21,34,55]

squared_numbers =[number*number for number in numbers]

print(squared_numbers)

even_numbers = [number for number in numbers if number%2 == 0]
print(even_numbers)

import pandas

list_one = [1,2,3,4,5,6,4,5,3,4,78,76,56,44,55,43,]
list_one