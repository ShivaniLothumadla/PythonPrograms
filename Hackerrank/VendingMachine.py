import os
import random
import re
import sys
# num_items, item_coins = map(int, input().split())

# def __init__(self, num_items, item_coins):
#     self.num_items = num_items
#     self.item_coins = item_coins
# i = 10
# j = 2

def machine():
    items = 10
    coins = 2
    return items, coins

i, j = machine()

def buy(num_items, num_coins):

    if num_items <= globals()['i'] and num_coins >= num_items * j:
        globals()['i'] = globals()['i'] - num_items
        return num_coins - (num_items * j)

    elif num_items > globals()['i'] and num_coins >= num_items * j:
        return 'Not enough items in the machine'

    elif num_items <= globals()['i'] and num_coins < num_items * j:
        return 'Not enough coins'

n = int(input())
for _ in range(n):
    num_items, num_coins = map(int, input().split())
    change = buy(num_items, num_coins)
    print(change)

