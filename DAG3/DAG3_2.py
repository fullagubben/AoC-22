with open('LIST3.txt', 'r') as f:
    lines = f.readlines()
    rucksacks = [entry.strip() for entry in lines]
numberlist = []
matches = []
total = 0
number = 0
for content in rucksacks:
    numberlist.append(content)
    number += 1
    if number == 3:
        number = 0        
        if set(numberlist[0]) & set(numberlist[1]) & set(numberlist[2]):
            matches = str(set(numberlist[0]).intersection(set(numberlist[1]),set(numberlist[2])))
            points = (ord((matches[2])))
            if points > ord('a'):
                total += points - 96
            else:
                total += points -38
            numberlist = []
print (total)