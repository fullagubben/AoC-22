with open('LIST3.txt', 'r') as f:
    lines = f.readlines()
    rucksacks = [entry.strip() for entry in lines]
matches = []
total = 0
for content in rucksacks:    
    firstpart, secondpart= content[:len(content)//2], content[len(content)//2:]
    firstpartset = set(firstpart)
    secondpartset = set(secondpart)
    if set(firstpart) & set(secondpart):
        matches = str(firstpartset.intersection(secondpartset))
        points = (ord(matches[2]))
        if points > ord('a'):
            total += points - 96
        else:
            total += points -38
print(total)
