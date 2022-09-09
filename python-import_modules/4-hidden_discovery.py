#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":

    avoid = "__"
    for x in range(1, len(dir(hidden_4))):
        if avoid not in dir(hidden_4)[x]:
            print(dir(hidden_4)[x])
