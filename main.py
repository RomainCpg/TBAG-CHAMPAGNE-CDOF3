import json
from utils import *

if __name__ == '__main__':

    input = 0
    read_lines("starting")

    input = read_and_get_choices("starting")

    while True:
        read_lines(input)

        input = read_and_get_choices(input)

