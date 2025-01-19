# TBAG-CHAMPAGNE-CDOF3
This project is about a text-based adventure game. The player will have multiple decision to make...

# Python Text-Based Adventure Game

## Overview
This is a simple text-based adventure game implemented in Python. The game allows players to make choices that influence the progression of the story, which is stored in a JSON file.

## Features
- Dynamic story progression based on player choices.
- Easy-to-modify story structure stored in `story.json`.
- Interactive gameplay with input validation.

### File Descriptions
- **main.py**: The main script that runs the game, handles user input, and manages story progression.
- **story.json**: A structured JSON file where the story, dialogue, and choices are defined.
- **utils.py**: Contains helper functions for reading and displaying story text and handling user input.

## How to Run the Game
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Ensure you have Python installed (version 3.6 or higher).
3. Run the game:
   ```bash
   python main.py
   ```

## How to Customize the Story
1. Open the `story.json` file.
2. Add or modify story steps using the following structure:
   ```json
   {
     "step_name": {
       "lines": ["Line 1", "Line 2"],
       "choices": [
         ["Choice text", "next_step"],
         ["Another choice", "another_step"]
       ]
     }
   }
   ```
3. Save the file and rerun the game.

## Example Story
Here is a snippet from `story.json`:
```json
"starting": {
  "lines": [
    "You wake up alone in the middle of your prison cell...",
    "Suddenly, you hear the sound of keys and..."
  ],
  "choices": [
    ["1 - Close your eyes.", "eat_death"],
    ["2 - Accept your meal.", "destination"]
  ]
}
```

## Contribution
Feel free to fork this repository and submit pull requests for new features or story updates. Contributions are always welcome!

## License
This project is licensed under the MIT License. See the LICENSE file for details.

