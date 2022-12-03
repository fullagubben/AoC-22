with open('LIST2.txt', 'r') as f:
    lines = f.readlines()
    games = [entry.strip() for entry in lines]



player1 = 0
player2 = 0
lines = 0
for game in games:
    lines += 1
    if game == "A Z":
        player1 += 1+6  # won with rock
        player2 += 3    # lost with scissor
    elif game == "C Y":
        player1 += 3+6 # won with scissor
        player2 += 2   # lost with paper
    elif game == "B X":
        player1 += 2+6 # won with paper
        player2 += 1    # lost with rock
    elif game == "A X": # lika med rock
        player1 += 1+3
        player2 += 1+3
    elif game == "B Y": # lika med paper
        player1 += 2+3
        player2 += 2+3   
    elif game == "C Z": # lika med scissor
        player1 += 3+3
        player2 += 3+3
    elif game == "C X":
        player1 += 3+0 # lost with scissor
        player2 += 1+6 # won with rock
    elif game == "B Z":
        player1 += 2+0 # lost with paper
        player2 += 3+6 # won with scissor
    elif game == "A Y":
        player1 += 1+0 # lost with rock
        player2 += 2+6 # won with paper

#X for Rock, Y for Paper, and Z for Scissors.
#A for Rock, B for Paper, and C for Scissors.
#1 for Rock, 2 for Paper, and 3 for Scissors)

#X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
# R-S
# S-P 
# P-R

print(player1)
print(player2)
print(lines)








