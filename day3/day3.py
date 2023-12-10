
def checkIfPart(start, end, row):

    #print(f"\n \npart number found from [{start} to {end}] in row: [{row}]", end="\t")
    boxStart = [row - 1 if row > 0 else row, start - 1 if start >0 else start]
    boxEnd = [row + 1 if row < len(matrix[row])-1 else row, end + 1 if end < len(matrix)-1  else end]
    #print(f"box for checking {boxStart}, {boxEnd}")
    found = False
    print(f"row {row} bs {boxStart} - be {boxEnd}")
    for i in range(boxStart[0], boxEnd[0] + 1):
        print("")
        for j in range(boxStart[1], boxEnd[1] + 1):
            if(not matrix[i][j] == "." and not matrix[i][j].isdigit()):
                found =  True
            print(matrix[i][j], end=" ")
    
    return found

with open('day3/input.txt', 'r') as file:
    lines = file.readlines()

cols = len(lines[0].strip())
rows = len(lines)

sumOfParts = 0

print(f"cols: {cols}, rows: {rows}")

matrix = [[line.strip() for line in lines[i]] for i in range(len(lines))]

for row in range(rows):
    start = -1
    end = -1
    for col in range(cols):
        if(matrix[row][col].isdigit() and start==-1):
            start = col
        if( (col == len(matrix[row])-1 or not matrix[row][col+1].isdigit()) and start!=-1):
            end = col
        if(start != -1 and end != -1):
            if(checkIfPart(start, end, row)):
                enginePartNumber = ''.join(matrix[row][c] for c in range(start, end+1))
                print(f"valid part number at [{row},{col-1}] no: {enginePartNumber}")
                sumOfParts += int(enginePartNumber)
            else:
                print(f"XXXXXXXXXXXXXXXXXXXXXXXXXX [{row},{col}]")
            start = end = -1
        


        
print(f"rows {len(matrix)} cols {len(matrix[0])} Total Sum: {sumOfParts}")