# Simple Game of Life which is based on Conway's Game of Life.
Link to Conway's Game of Life: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

Gameplay is simple: A cell can be living or dead. Once it is intialized with a 1 in 3 chance of being "living". Once the game board size is set it is filled with random cells. Then between every iteration of the game each cell is updated. If it has less than 2 or more than 3 living neighbors it "dies". If it is "dead" then it needs at least 3 living neighbors to come back to life.

I have handled edge cases and updating of the cells neighbors between generations.

This runs from the terminal and has no graphical user interface. In order to run the game you can type into your terminal: python3 hovedprogram.py

Code is written in Norwegian, while gameplay language is in English.

***Usage: python3 hovedprogram.py***

This starts the game. You can choose how many rows and columns the gameboard will have. It is beneficial to have more than 10 rows and columns in order to see a pattern develop.

Once the game is started you can press ENTER in order to continue to the next generation or type q in order to quit.

### Enjoy!

Please reach out with any comments or feedback. I'd love to hear from you!

