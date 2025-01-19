import json
import os

# Get the current working directory
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def read_lines(story_step_name: str):
    os.system('cls||clear')
    with open(os.path.join(ROOT_DIR, 'story.json'), "r") as f:
        story = json.load(f)
        lines_to_print = story[story_step_name]["lines"]

        for index, lines in enumerate(lines_to_print):
            print(lines)
            if index != len(lines_to_print) - 1:
                input("Press \'any key\' to continue...")


def read_and_get_choices(story_step_name: str) -> int:
    with open(os.path.join(ROOT_DIR, 'story.json'), "r") as f:
        story = json.load(f)
        choices_to_print = story[story_step_name]["choices"]

        for choice in choices_to_print:
            print(choice[0])

        choice_value = int(input("What's your choice ? "))

        while choice_value < 1 or choice_value > len(choices_to_print):
            choice_value = int(input("Invalid choice number, please, make another one... "))

        next_step = choices_to_print[choice_value - 1][1]

        if next_step == "":
            print("Goodbye!")
            exit()

        return next_step

