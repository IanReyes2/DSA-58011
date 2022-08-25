list1 = [26,49,98,87,62,75]

only_odd = [num for num in list1 if num % 2 == 1]
res = sum(only_odd)

print("Odd Numbers are: ",only_odd)
print("The Sum is: ", res)
