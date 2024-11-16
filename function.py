import pandas as pd

list_search = []
c = ""

def Search(x):
    global list_search, c
    c = input("Enter the keyword to search: ")
    list_search = [item for item in x if c.lower() in item.lower()]
