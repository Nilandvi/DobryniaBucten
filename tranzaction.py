from settings import *
from shop_price import *


def tranz(name):
    item = next((item for item in lst if item["name"] == name), None)
    product = int(lines[14][0]) + int(item["count"])
    money = int(lines[8]) + int(item["count"])
    braga = int(lines[40]) + int(item["count"])
    if int(lines[2]) >= item["price"][0] and int(lines[4]) >= item["price"][1] and int(lines[6]) >= item["price"][2] and  int(lines[8]) >= item["price"][3]:
        oak, rock, clay, coin = int(lines[2]) - item["price"][0], int(lines[4]) - item["price"][1], int(lines[6]) - item["price"][2], int(lines[8]) - item["price"][3]
        lines[2] = lines[2].replace(lines[2], str(oak) + '\n')
        lines[4] = lines[4].replace(lines[4], str(rock) + '\n')
        lines[6] = lines[6].replace(lines[6], str(clay) + '\n')
        lines[8] = lines[8].replace(lines[8], str(coin) + '\n')
        if name == "barup_lvl1" or name == "barup_lvl2" or name == "barup_lvl3":
            lines[14] = lines[14].replace(lines[14], str(product) + '\n')
        if name == "clay" or name == "stone" or name == "wood":
            lines[8] = lines[8].replace(lines[8], str(money) + '\n')
        if name == "boost":
            lines[16] = lines[16].replace(lines[16], "1" + '\n')
        if name == "fruit":
            lines[40] = lines[40].replace(lines[40], str(braga) + '\n')
        with open('base.txt', 'w') as fi:
            fi.writelines(lines)
            fi.close
    else: print("У тебя денег")
