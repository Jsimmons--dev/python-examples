#list comp with range
list = [i for i in range(5)]
print(list)

#list comp with filter
list = [i for i in range(5) if  i % 2 == 0]
print(list)

#more complex expression
list = [i * i for i in range(6)]
print(list)