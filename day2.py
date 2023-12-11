"""
--- Day 2: Cube Conundrum ---
You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf runs over to greet you.

The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. They don't get many visitors up here; would you like to play a game in the meantime?

As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.

To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
"""

import re

def game():
    # result list for all the game IDs
    result = []
    # pattern for game id   
    p = re.compile(r'\d+(?=:)')
    # checker dictionary
    d = {"blue": 14, "red": 12, "green": 13}
    # create pattern to get individual color numbers in a list
    p_blue = re.compile(r'\d+ (?=blue)')
    p_red = re.compile(r'\d+ (?=red)')
    p_green = re.compile(r'\d+ (?=green)')

    # read the file

    with open('game1.txt', 'r') as file:
        for line in file.readlines():
            b = p_blue.findall(line)
            g = p_green.findall(line)
            r = p_red.findall(line)
            # actual list with the correct color cubes
            lis_blue = [i for i in b if int(i) <= d['blue']]
            lis_green = [j for j in g if int(j) <= d['green']]
            lis_red = [k for k in r if int(k) <= d['red']]

            if len(b) == len(lis_blue) and len(lis_green) == len(g) and len(r) == len(lis_red):
                result.extend(p.findall(line))
    # sum of the game ids
    total = 0
    for id in result:
        total += int(id)

    return total

if __name__ == '__main__':
    print(game())

            
