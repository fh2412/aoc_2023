import re

input = "C:\\TEMP\\AOC\\2023\\01\\01_input.txt"
#input = "C:\\TEMP\\AOC\\2023\\01\\testCase.txt"

with open(input, 'r') as input:
    data = (input.read()).strip().split()

result = 0
for string in data:
    first = ""
    last = ""
    for char in string:
        if (char.isdigit()) and first == "":
            first = char
        if (char.isdigit()):
            last = char

    number = int(str(first) + (str(last)))
    result += number

print(result)
