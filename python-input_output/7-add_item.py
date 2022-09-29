#!/usr/bin/python3
"""Learning how to use JSON"""
import json
from sys import argv
load_from = __import__("6-load_from_json_file").load_from_json_file
save_file = __import__("5-save_to_json_file").save_to_json_file
file = "add_item.json"
try:
    Plist = load_from(file)
except FileNotFoundError:
    Plist = []

save_file(Plist + argv[1:], file)
