num_value = int(input("how much number will be in the list? "))
lists = []
i = 0
while i < num_value:
    numbers = int(input("give the values: "))
    i += 1
    lists.append(numbers)
    print(numbers)

maks = lists[0]
for num in lists:
    if num > maks:
        maks = num
print(f"the biggest number is {maks}")




