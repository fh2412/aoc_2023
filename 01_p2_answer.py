import re

input = "C:\\TEMP\\AOC\\2023\\01\\02_input.txt"
#input = "C:\\TEMP\\AOC\\2023\\01\\testCase.txt"

with open(input, 'r') as file:
    data = file.read().strip().split()

pattern = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

result=0
for line in data:
    numbers = []
    #loop through each pos. in line
    for i, value in enumerate(line):
        
        #check if current value is a digit
        if value.isdigit():
            numbers.append(value)
    

        for counter, patternItem in enumerate(pattern):
            print("counter:", counter , " | used patternItem: ", patternItem, " | string on pos i: ", line[i:])
            #check for each char in line, if the patternitem is matching
            if(line[i:].startswith(patternItem)):
                
                numbers.append(counter) # +1 needed if pattern doesnt start a 'zero'
    print(numbers)

    #add numbers as strings
    newNumber = str(numbers[0]) + str(numbers[-1])
    #parse to int and add it to result
    result += int(newNumber)
    break

print(result)
