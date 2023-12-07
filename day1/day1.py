import re

def intToNumbers(line, index, result):

    searchline = line[index:] 

    if (len(line) - index < 1):
        return result

    elif (searchline.startswith('one')):
        result += '1'
        return intToNumbers(line, index+1, result)

    elif (searchline.startswith('two')):
        result += '2'
        return intToNumbers(line, index+1, result)
    
    elif (searchline.startswith('three')):
        result += '3'
        return intToNumbers(line, index+1, result)
    
    elif (searchline.startswith('four')):
        result += '4'
        return intToNumbers(line, index+1, result)
    
    elif (searchline.startswith('five')):
        result += '5'
        return intToNumbers(line, index+1, result)

    elif (searchline.startswith('six')):
        result += '6'
        return intToNumbers(line, index+1, result)

    elif (searchline.startswith('seven')):
        result += '7'
        return intToNumbers(line, index+1, result)

    elif (searchline.startswith('eight')):
        result += '8'
        return intToNumbers(line, index+1, result)

    elif (searchline.startswith('nine')):
        result += '9'
        return intToNumbers(line, index+1, result)
    else: 
        result += line[index]
        return intToNumbers(line, index+1, result)



with open('day1/input.txt', 'r') as file:
    lines = file.readlines()

count = 0

for line in lines:
    convertedLine = intToNumbers(line, 0, "")
    numbers = re.findall("[1-9]", convertedLine)
    if ( len(numbers) > 0 ):
        print("\n\n\n",line, convertedLine, numbers, str(int(numbers[0] + numbers[len(numbers) - 1 ])), count + int(numbers[0] + numbers[len(numbers) - 1 ]), end="\t")
        count+= (int(numbers[0] + numbers[len(numbers)-1]))

print(count)

