""" 
Advent of Code | Day 02
Part 1 & 2
"""
import re

def day02():
    path = "C:\\workplace\\AOC_2023\\02\\02_p1_input.txt"
    #path = "C:\\workplace\\AOC_2023\\02\\02_p1_sample.txt"
    with open(path, 'r') as file:
        input = file.readlines()
  
    gameCounter = 0
    game2Counter = 0
    for line in input:

        gameID, draws = line.split(':')
        gameID = int(gameID.split(' ')[-1])
        state = {'red': 0, 'green': 0, 'blue': 0}
        possible = True

        #only needed for part2
        min_possible_draw = {'red': 0, 'green': 0, 'blue': 0}

        for draw in draws.split(';'):
            for cubes in draw.strip().split(', '):
                max_values = {'red': 12, 'green': 13, 'blue': 14}
                value, color = cubes.split(' ')
                value = int(value)

                #only needed for part2
                if value > min_possible_draw[color]:
                    min_possible_draw[color] = value
                

                # update color value on dict
                if state[color] == 0:
                    state[color] = value
                else:
                    #if color alrd. exists, add value instead of overwriting
                    state[color] += value
                
                #check if current value of the draw is higher then the maximum allowed value
                if int(value) > max_values[color]:
                    #print(f"_value to high_{value, color} max_value:{state[color]}")
                    possible = False

        #print entire dict (be aware, this is the entire sum of each game! variable "possbile" will be checked on each draw!)         
        #print(f"gameID: {gameID} state: {state}")

        if(possible):
            gameCounter += gameID

        #only needed for part2
        value_multiplied = 1   #1 because when i start with 0, it would be alw. 0 :'D
        for min_value in min_possible_draw.values():
            value_multiplied = value_multiplied * min_value

        game2Counter += value_multiplied
        
    print(gameCounter)
    print(game2Counter)


day02()
