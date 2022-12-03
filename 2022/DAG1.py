with open('LIST.txt', 'r') as f:
    lines = f.readlines()
    calories = [entry.strip() for entry in lines]



total = 0
most_calories = 0
list = []
for calorie in calories:
    if calorie != "":
        caloriess = int(calorie)
        total += caloriess
    else:
        if total > most_calories:
            
            list.append(total)
            most_calories = total
            total = 0
        else:
            
            list.append(total)
            total = 0
            
list.sort()

print(most_calories)

res = sum(list[-3:])

print(res)