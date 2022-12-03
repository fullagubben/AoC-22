with open('LIST2.txt', 'r') as f:
    lines = f.readlines()
    games = [entry.strip() for entry in lines]



player1 = 0
player2 = 0
lines = 0
for game in games:
    lines += 1
    if game == "A Z":   ## win
        player1 += 2+6  # won with paper
        player2 += 1    # lost with rock
    elif game == "C Y":    ## draw
        player1 += 3+3 # draw with scissor
        player2 += 3+3   # draw with scissor
    elif game == "B X":   ## loose
        player2 += 2+6 # won with paper
        player1 += 1+0    # lost with rock
    elif game == "A X": ## loose
        player1 += 3+0  # lost with scissor
        player2 += 1+6  # won with rock
    elif game == "B Y": ## draw
        player1 += 2+3   # draw with paper
        player2 += 2+3   # draw with paper
    elif game == "C Z": ## win
        player1 += 1+6  # won with rock
        player2 += 3  #lost with scissor
    elif game == "C X":   ## loose
        player1 += 2+0 # lost with paper
        player2 += 1+6 # won with rock
    elif game == "B Z": ## win
        player1 += 3+6 # won with scissor
        player2 += 2 # lost with paper
    elif game == "A Y":     ## draw
        player1 += 1+3 # draw with rock
        player2 += 1+3 # draw with rock

#X for Rock, Y for Paper, and Z for Scissors.
#A for Rock, B for Paper, and C for Scissors.
#1 for Rock, 2 for Paper, and 3 for Scissors)

#  X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
# R-S
# S-P 
# P-R

print(player1)
print(player2)
print(lines)








