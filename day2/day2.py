import re

redMax = 12
greenMax = 13
blueMax = 14

gameIdSum = 0

with open('day2/input.txt', 'r') as file:
    lines = file.readlines()

### part 1
for line in lines:
    game_number = int(re.findall(r'\b\d+\b',line.split(":")[0])[0])
    sets_revealed = line.split(":")[1].replace(";",",").strip().split(", ")
    found = False
    for set_revealed in sets_revealed:
        amount = int(set_revealed.split(" ")[0])
        color = set_revealed.split(" ")[1]
        if ( color == "red" and amount>redMax or color == "green" and amount>greenMax or color == "blue" and amount>blueMax):
            print(f"Invalid game {game_number} with {amount} {color}")
            found = True
            break
    
    if(not found):
        gameIdSum += game_number

###part2

sumPower = 0

for line in lines:

    redMin = 0
    greenMin = 0
    blueMin = 0

    game_number = int(re.findall(r'\b\d+\b',line.split(":")[0])[0])
    sets_revealed = line.split(":")[1].replace(";",",").strip().split(", ")
    for set_revealed in sets_revealed:
        amount = int(set_revealed.split(" ")[0])
        color = set_revealed.split(" ")[1]
        if(color == "red" and redMin<amount):
            redMin = amount
        if(color == "green" and greenMin<amount):
            greenMin = amount
        if(color == "blue" and blueMin<amount):
            blueMin = amount
    
    sumPower += redMin * greenMin * blueMin
    print(f"min set of cubes is {redMin} red, {greenMin} green, {blueMin} blue, its power is {redMin * greenMin * blueMin}")

print(f"part one {gameIdSum} part two {sumPower}")


