
texts = 'move 8 from 2 to 1'


list = [['H', 'C', 'R', ' ', ' ', ' ', ' ', ' '], ['B', 'J', 'H', 'L', 'S', 'F', ' ', ' ']]
print (list)
def movedecrypter (data):
    result = data.split(' ')
    return int(result[1]), int(result[3]), int(result[5])

def craneoperator (movequant, movefrom, moveto):
    movefrom -= 1
    moveto -= 1
    list[moveto].extend(list[movefrom][:movequant])  # adds to list
    for i in range(movequant):    # removes from list
        list[movefrom].pop()

    print(list)

print(movedecrypter(texts))
craneoperator(movedecrypter(texts)[0],movedecrypter(texts)[1],movedecrypter(texts)[2])




