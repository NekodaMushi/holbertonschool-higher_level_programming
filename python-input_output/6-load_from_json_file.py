#!/usr/bin/python3
"""Learning how to use JSON"""
import json


def load_from_json_file(filename):
    """Object from a “JSON file”"""

    with open(filename, "r", encoding="UTF8") as f:
        return json.load(f)
